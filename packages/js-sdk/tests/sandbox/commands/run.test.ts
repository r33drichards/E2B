import { expect, assert } from 'vitest'

import { sandboxTest } from '../../setup.js'

sandboxTest('run', async ({ sandbox }) => {
  const text = 'Hello, World!'

  const cmd = await sandbox.commands.run(`echo "${text}"`)

  assert.equal(cmd.exitCode, 0)
  assert.equal(cmd.stdout, `${text}\n`)
})

sandboxTest('run with special characters', async ({ sandbox }) => {
  const text = '!@#$%^&*()_+'

  const cmd = await sandbox.commands.run(`echo "${text}"`)

  assert.equal(cmd.exitCode, 0)
  assert.equal(cmd.stdout, `${text}\n`)
})

sandboxTest('run with multiline string', async ({ sandbox }) => {
  const text = 'Hello,\nWorld!'

  const cmd = await sandbox.commands.run(`echo "${text}"`)

  assert.equal(cmd.exitCode, 0)
  assert.equal(cmd.stdout, `${text}\n`)
})

sandboxTest('run with timeout', async ({ sandbox }) => {
  const cmd = await sandbox.commands.run('echo "Hello, World!"', { timeoutMs: 1000 })

  assert.equal(cmd.exitCode, 0)
})

sandboxTest('run with too short timeout', async ({ sandbox }) => {
  await expect(sandbox.commands.run('sleep 10', { timeoutMs: 1000 })).rejects.toThrow()
})


sandboxTest('can disconnect and reconnect with logs', async ({ sandbox }) => {
  const cmd = await sandbox.commands.run(`
  echo "start"

  # some command that periodically logs to stdout 5 times
  for i in {1..5}; do
    date +%s%3N
    sleep 1
  done

  echo "end"
  `, {
    background: true,


  })

  // sleep for 2 seconds to make sure command starts and does work
  await new Promise(resolve => setTimeout(resolve, 2000))


  let { timestamp } = await cmd.disconnect()

  let out: string[] = []

  const reconnectedCmd = await sandbox.commands.connect(
    cmd.pid,
    {
      eventsSince: timestamp,
      onStdout: e => { out.push(e) },
    }
  )

  // assert end not in out
  out.map(e => assert.notEqual(e, 'end\n'))

  // wait for the command to finish
  await reconnectedCmd.wait()


  // check the output
  // assert start not in out
  out.map(e => assert.notEqual(e, 'start\n'))
  // assert end in out
  assert(out.reduce((acc, e) => acc || e === 'end\n', false))
  const filtered = out.filter(e => e !== 'end\n').map(e => parseInt(e.trim()))
  // filtered should be less then 5 elements
  assert(filtered.length  < 5)
  let milliseconds = Date.parse(timestamp)
  assert(filtered.reduce((acc, e) => acc && (e > milliseconds), true))
})

// make a test to reconnect to a command that has already finished and  make sure logs 
// are not streamed
// also tests the envd can receive a request w/o supplying timestamp 
sandboxTest('can disconnect and reconnect to a finished command', async ({ sandbox }) => {
  const cmd = await sandbox.commands.run(`
  echo "start"
  for i in {1..5}; do
    date +%s%3N
    sleep 1
  done
  echo "end"
  `, {
    background: true,
  })

  await cmd.disconnect()

  let out: string[] = []

  const reconnectedCmd = await sandbox.commands.connect(
    cmd.pid,
    {
      onStdout: e => { out.push(e) },
    }
  )


  // wait for the command to finish
  await reconnectedCmd.wait()

  // check the output
  // assert start not in out
  out.map(e => assert.notEqual(e, 'start\n'))
  // assert end in out
  assert(out.reduce((acc, e) => acc || e === 'end\n', false))

  
})
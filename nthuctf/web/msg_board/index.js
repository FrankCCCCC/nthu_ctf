const express = require("express")
const timeout = require("connect-timeout")
const fs = require("fs")
const { type } = require("os")

const port = process.env.PORT || 80

const app = express()
var record = "";

app.use(timeout("5s"))

app.get("/", (req, res) => {
    console.log(`${JSON.stringify(req.query)}`)

    record = record + `${JSON.stringify(req.query)}\n`
    res.send(Math.random().toString())
})

app.get("/logs", (req, res) => {
    let str = record.toString()
    res.send(str)
})

app.listen(port, () => {
    console.log(`MSG_BOARD Server is Listening on ${port}`)
})
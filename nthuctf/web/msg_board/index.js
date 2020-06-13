const express = require("express")
const fs = require("fs")
const port = process.env.PORT || 80

const app = express()

app.get("/", (req, res) => {
    fs.writeFile('./out.txt', req.params, (err) => {
		if (err) throw err
    })
    
    res.status(200)
})

app.listen(port, () => {
    console.log(`MSG_BOARD Server is Listening on ${port}`)
})
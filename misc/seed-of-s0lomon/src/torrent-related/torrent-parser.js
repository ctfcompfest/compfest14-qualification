//torrent-parser

const parse = require("parse-torrent");
const fs = require("fs");


const result = parse(fs.readFileSync("./mafteah_shelomoh.torrent"));
console.log(result);
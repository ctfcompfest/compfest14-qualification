const create = require("create-torrent");
const fs = require("fs");

create("./nadenka.txt",{
	pieceLength:2,
	private: true,
	announceList : [[""]],
	urlList : [[""]],
},(err, torrent) => {
	if (!err) {
		fs.writeFile("mafteah_shelomoh.torrent", torrent, (err, res) => {
			if(err) console.log(err);
		})
		}
		else{
			console.log(err);
		}
})
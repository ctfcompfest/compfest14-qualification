import express from "express";
import {Bucket} from './middlewares/bucket.js';

function rateLimitPerUser(maxBurst, fillRatePerSecond) {
	const userBuckets = new Map()
	
	return function expressMiddleware(req, res, next) {
	  let reqIP = req.headers["x-real-ip"];
	  if (!userBuckets.has(reqIP)) {
		console.log('Creating for bucket for user ' + reqIP)
		userBuckets.set(reqIP, new Bucket(maxBurst, fillRatePerSecond))
	  }
	  const currentUserBucket = userBuckets.get(reqIP)
	  if (currentUserBucket.requestToken()) {       
		next()     
	  } else {
		res.status(429).json(
			{
			status : 429, 
			data : {},
			message :'IP '+ reqIP +' not allowed because not enough token, token fill rate is '+ fillRatePerSecond*60+'/minute. You have: '+ userBuckets.get(reqIP).tokens+' token :('
			});     
	  } 
	}
  }

const app = express();
const port = 3000;

app.use(express.json());
app.post("/validate",
rateLimitPerUser(2, 0.0055555555555556), // 2 tokens max, about 0.0055555555555556 tokens added each second, 
(req, res) => {
	if(req.body.username === `n4denka_69` && req.body.password === `nadenka_w4nts_some_1ce_cre4m` && req.body.offering === `gl1da` && req.body.isNight){
		return res.status(200).json(
			{
			status : 200, 
			data : {
				token : "07c842f422bf7cc106fff94e55e3812af98b91e99a192b8d85283a185765d71e",
				user : "n4denka_69",
				pass : "nadenka_w4nts_some_1ce_cre4m",
				}, 
			message : "successful auth"
			});
	}else{
		return res.status(401).json({status : 401,  message : "invalid credentials."});
	}
});

app.post("/auth", (req, res) => {
	if (req.body.token == "07c842f422bf7cc106fff94e55e3812af98b91e99a192b8d85283a185765d71e") {
		return res.status(200).json({
			status : 200, 
			data : {
				flag : "COMPFEST14{n4denk4_l1kes_1ce_cre4m_ea62b43b0e}",
			}, 
			message : "successful auth"})
	}else{
		return res.status(401).json({
			status: 401, 
			data : {}, 
			message : "invalid credentials."})
	}
});


app.listen(port, () => console.log(`Listening on port ${port}.`));

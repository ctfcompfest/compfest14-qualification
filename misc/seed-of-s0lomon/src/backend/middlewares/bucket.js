export class Bucket {
    constructor(maxBurst, fillRatePerSecond) {
      this.maxBurst = maxBurst
      this.fillRatePerSecond = fillRatePerSecond
      this.lastRefreshed = Math.floor(Date.now() / 1000)
      this.tokens = maxBurst
    }
    requestToken() {
      this.refreshTokens()
      if (this.tokens >= 1) {
        this.tokens--
        console.log('Removed a token, '+this.tokens+' left.')
        return true
      }
    }
    refreshTokens() {
      // Gets current timestamp
      const now = Math.floor(Date.now() / 1000)
      // Calculates time since last refresh
      const timeSinceLastRefresh = now - this.lastRefreshed
      // Calculates amount of tokens to be added
      const addedTokens = timeSinceLastRefresh * this.fillRatePerSecond
      // Adds tokens
      this.tokens += addedTokens
      // Makes sure bucket doesn't have more tokens than maximum allowed 
      this.tokens = (this.tokens > this.maxBurst) ? this.maxBurst : this.tokens
      // Updates timestamp
      this.lastRefreshed = now
    }
  }
  
  function rateLimit(maxBurst, fillRatePerSecond) {   
    const tokenBucket = new Bucket(maxBurst, fillRatePerSecond)   
    return function expressMiddleware(req, res, next) {     
      if (tokenBucket.requestToken()) {       
        next()     
      } else {
        res.status(429).send('not allowed')     
      }   
    }
  }
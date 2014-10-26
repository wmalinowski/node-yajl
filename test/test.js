var assert = require("assert");
var yajl = require('../');

describe('YAJL', function(){
  describe('version no', function(){
    it('should be 2.1.0', function(){
      assert.equal(yajl.getYajlVersion(), 20100);
    })
  })
})
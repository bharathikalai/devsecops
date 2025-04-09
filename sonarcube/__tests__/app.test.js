const request = require('supertest');
const app = require('../app');

describe('GET /', () => {
  it('should return Hello my Dear thala!', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toBe('Hello my Dear thala!');
  });
});



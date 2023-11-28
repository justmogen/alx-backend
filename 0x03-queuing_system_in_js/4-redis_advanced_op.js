import redis from'redis';
const client = redis.createClient();

client
	.on('connect', () => {
	console.log('Redis client connected to the server');
})
	.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

const name = "HolbertonSchools";
const values = {
	Portland: 50,
	Seattle: 80,
	"New York": 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2,
};
for (const [key, valu] of Object.entries(values)) {
	client.hset(name, key, valu, (_, respo) => redis.print(`Reply: ${respo}`));
}

client.hgetall(name, (_, object) => console.log(object));

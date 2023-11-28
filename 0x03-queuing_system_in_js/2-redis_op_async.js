import redis from'redis';
import { promisify } from 'util';

const client = redis.createClient();
const asyncGet = promisify(client.get).bind(client);

client
	.on('connect', () => {
	console.log('Redis client connected to the server');
})
	.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, respo) => {
		redis.print(`Reply: ${respo}`);
	});
}

async function displaySchoolValue(schoolName) {
	const respo = await asyncGet(schoolName);
	console.log(respo);
}

(async () => {
	displaySchoolValue("Holberton");
	setNewSchool("HolbertonSanFrancisco", "100");
	displaySchoolValue("HolbertonSanFrancisco");
})();

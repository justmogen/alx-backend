import redis from'redis';
const client = redis.createClient();

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

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, respo) => {
		console.log(respo);
	});
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

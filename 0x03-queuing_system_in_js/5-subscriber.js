import redis from "redis";

const client = redis.createClient();

client
  .on("error", (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
    client.quit(); // Quit the Redis connection on error
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
    client.subscribe("holberton school channel");
  });

// Event listener for messages received on the subscribed channel
client.on("message", (channel, message) => {
  console.log(message);

  // Unsubscribe and quit if the message is "KILL_SERVER"
  if (message === "KILL_SERVER") {
    client.unsubscribe("holberton school channel");
    client.quit();
  }
});


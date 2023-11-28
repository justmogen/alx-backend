import kue from 'kue';

const queue = kue.createQueue();
const objjob = {
	phoneNumber: '123456789',
	message: 'This is the code to verify your account',
};

const queueNot = 'push_notification_code';

const job = queue.create(queueNot, objjob).save((err) => {
	if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
	console.log('Notification job completed');
});

job.on('failed', () => {
	console.log('Notification job failed');
});

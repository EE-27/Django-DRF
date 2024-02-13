Task
	Context
		In 2018, James Clear wrote a book called Atomic Habits, which is about acquiring new useful habits and eradicating old bad habits. A customer has read the book, is impressed, 		and asks you to implement a healthy habits tracker.

As part of your coursework project, implement the backend part of the SPA web application.

	Criteria for acceptance of coursework
	CORS has been configured.
	Configured integration with Telegram.
	Implemented pagination.
	Utilized environment variables.
	All necessary models described or redefined.
	All necessary endpoints implemented.
	All necessary validators have been configured.
	Described access rights are laid down.
	Pending tasks via Celery have been configured.
	The project has been covered by tests at least 80%.
	The code is organized according to the best practices.
	A list of dependencies is available.
	Flake8 test result is 100% when migrations are excluded.
	The solution has been posted on GitHub.

Watch the video, it will help you with your coursework.

<<video>>

Task Description
	Add the necessary habit models.
	Implement endpoints to work with the frontend.
	Create an application to work with Telegram and reminder newsletters.

Models
	In the book, a good example of a habit is described as a specific action that can be fit into a single sentence:

I will [ACTION] at [TIME] at [PLACE].

	For every useful habit, you should reward yourself or make a pleasant habit immediately afterward. But the habit should not take more than 2 minutes to complete. Based on this we get 	the first model - Habit.

Habit:
	User - the creator of the habit.
	Place - the place where the habit should be performed.
	Time - the time when the habit should be performed.
	Action - the action that the habit represents.
	A sign of a pleasurable habit - a habit that can be tied to the performance of a useful habit.
	Linked habit - a habit that is linked to another habit, it is important to specify for useful habits but not for pleasant habits.
	Frequency (daily by default) - the frequency of the habit fulfillment for the reminder in days.
	Reward - what the user should reward themselves with after doing the habit.
	Time to complete - the amount of time the user is expected to spend on completing the habit.
	Sign of publicity - habits can be shared so that other users can take other users' habits as an example.
	Note that you may have more than one habit in your project.

Validators
	Eliminate simultaneous selection of a related habit and reward indication.
	The execution time should be no longer than 120 seconds.
	Only habits with the attribute of a pleasant habit can be included in linked habits.
	A pleasant habit cannot have a reward or a linked habit.
	A habit cannot be performed less frequently than once every 7 days.

Pagination
	To display the list of habits, implement pagination with 5 habits per page.

Access rights
	Each user has access only to their habits by the CRUD mechanism.
	The user can see a list of public habits without the ability to edit or delete them in any way.

Endpoints
	Registration
	Authorization
	List of current user's habits with pagination
	List of public habits
	Creating a habit
	Editing a habit
	Deleting a habit

Integration
	To make the service fully functional, it is necessary to implement work with pending tasks to remind you of the time when you need to perform your habits.

	To do this, you will need to integrate the service with Telegram messenger, which will send notifications.

<<Instructions for integration with Telegram>>

Security
	CORS must be configured for the project so that the frontend can connect to the project on the deployed server.

Documentation
	Documentation output must be configured for frontend developers to implement the screens. If necessary, manually describe endpoints for which documentation will not be generated 	automatically.

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Function used to keep the program running after creating
 * the zombie processes.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1); /* Sleep for 1 second to prevent high CPU usage */
	}
	return (0);
}

/**
 * main - Entry point for the program.
 * Description - Creates five zombie processes.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	int i, pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0); /* Child process exits after creating a zombie */
		}
	}
	infinite_while(); /* Parent process enters an infinite loop */
	return (0);
}

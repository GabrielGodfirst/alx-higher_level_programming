#include "lists.h"
#include <stdlib.h>

/**
 * free_dlistint - free a list
 * @head: list
 * Return: Void
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;

	while (current != NULL)
	{
		dlistint_t *temp = current;

		current = current->next;
		free(temp);
	}
}

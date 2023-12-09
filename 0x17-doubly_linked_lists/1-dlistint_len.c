#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * dlistint_len - Return list len
 * @h: struct list
 * Return: list_len
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		h = h->next;
		count++;
	}

	return (count);
}


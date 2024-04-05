#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function inserts a number into a sorted singly linked list
 * @head: linkedlist head
 * @number: node's value
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
	}
	else if (current->n >= number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next && current->next->n < number)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - chack if list is cyclic
 * @list: the head of our list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);

}

#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the singly linked list
 *
 * Return: 0 if the linked list is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (!head || !(*head))
		return (1);

	start = *head;
	len = listint_len(start);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;

	for (; i < len_cyc; i += 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);

		len_list -= 2;
	}

	return (1);
}

/**
 * get_nodeint_at_index - Retrieves a node at a specified index
 * @head: Pointer to the head of the linked list
 * @index: The index of the node to be retrieved
 *
 * Return: The node at the specified index, or NULL if it doesn't exist
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	while (current != NULL)
	{
		if (iter_times == index)
			return (current);

		current = current->next;
		++iter_times;
	}

	return (NULL);
}

/**
 * listint_len - Counts the number of nodes in a linked list
 * @h: Pointer to the linked list
 *
 * Return: Number of nodes in the linked list
 */
size_t listint_len(const listint_t *h)
{
	size_t length = 0;

	while (h != NULL)
	{
		++length;
		h = h->next;
	}

	return (length);
}

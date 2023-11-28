#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer of the head node
 * @number: value to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head, *new_node_to_insert;

	new_node_to_insert = malloc(sizeof(listint_t));
	if (new_node_to_insert == NULL)
		return (NULL);

	new_node_to_insert->n = number;

	if (!current_node || current_node->n >= number)
	{
		new_node_to_insert->next = current_node;
		*head = new_node_to_insert;
		return (new_node_to_insert);
	}

	while (current_node && current_node->next && current_node->next->n < number)
	{
		current_node = current_node->next;
	}

	new_node_to_insert->next = current_node->next;
	current_node->next = new_node_to_insert;

	return (new_node_to_insert);
}

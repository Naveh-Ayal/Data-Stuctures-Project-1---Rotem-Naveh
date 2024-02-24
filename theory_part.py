def generate_avl_trees_and_split():
    import random
    from interactive_tree import AVLTree, AVLNode

    results = []

    for i in range(1, 11):  # Loop through 1 to 10
        print("i: "+str(i))
        tree_size = (2 ** i) * 1000  # Calculate tree size
        avl_tree_rand = AVLTree()  # Initialize AVL Tree
        avl_tree_max = AVLTree()  # Initialize AVL Tree

        numbers = list(range(1, tree_size + 1))
        random.shuffle(numbers)

        # Insert numbers 1 to tree_size into the AVL tree
        for num in numbers:
            avl_tree_rand.insert(num, num)  # Inserting numbers
            avl_tree_max.insert(num, num)  # Inserting numbers

        # Process 1: Split by a random number
        random_split_key = random.randint(1, tree_size)  # Random key for splitting
        random_node = avl_tree_rand.search(random_split_key)  # Search for the node with the random key
        rand_key = random_node.get_key()
        split_result_random = avl_tree_rand.split_for_theory(random_node)  # Split the tree by the random key

        print("RANDOM SPLIT (chosen key: " + str(rand_key) + "):")
        print(split_result_random)

        # Process 2: Split by the maximal key of the left subtree
        # Find the maximal key in the left subtree by getting the rightmost node in the left subtree
        left_subtree_root = avl_tree_max.root.get_left()
        max_key_node = left_subtree_root
        while max_key_node.get_right().is_real_node():
            max_key_node = max_key_node.get_right()
        max_key = max_key_node.get_key()

        split_result_max_key = avl_tree_max.split_for_theory(max_key_node)  # Split the tree by the maximal key
        
        print("MAX SPLIT (chosen key: " + str(max_key) + "):")
        print(split_result_max_key)

        # Store the results
        #results.append({
        #    'tree_size': tree_size,
        #    'random_split_key': random_split_key,
        #    'split_result_random_sizes': (split_result_random[0].size(), split_result_random[1].size()),
        #    'max_key_split': max_key_node.get_key(),
        #    'split_result_max_key_sizes': (split_result_max_key[0].size(), split_result_max_key[1].size())
        #})

    return results

generate_avl_trees_and_split()

# Since the provided AVL tree implementation is quite large and complex, we'll run the function without
# actually executing the AVLTree code. This code block is meant to illustrate how you would integrate
# the tree generation and splitting processes using the provided AVLTree class and methods.
# To execute this for real, you would need to have the AVLTree and AVLNode classes defined as provided.
#username - Rotem & Naveh
#id1      - 211698824
#name1    - Rotem Kerem 
#id2      - 209207638
#name2    - Naveh Ayal 



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""calculates the height of node"""
	def calculate_height(self):
		hLeft = self.left.height #height of left child
		hRight = self.right.height #height of right child
		return max(hLeft, hRight) + 1
	
	
	"""calculates the Balance Factor of node"""
	def get_BF(self):
		return self.left.height - self.right.height 


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if (self.key == None):
			return False
		return True
	
	"""returns whether node is left child (if not - then right child)
	
	@rtype: bool
	@returns: True if self is left child, False if right.
	"""
	def is_left_child(self):
		if self.parent == None :
			return False
		if self.parent.left == self:
			return True
		return False
	

	###PRINT TREE FUNCTION######

	def display(self):
		lines, *_ = self._display_aux()
		for line in lines:
			print(line)

	def _display_aux(self):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
		# No child.
		if self.right is None and self.left is None:
			line = '%s' % self.key
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if self.right is None:
			lines, n, p, x = self.left._display_aux()
			s = '%s' % self.key
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if self.left is None:
			lines, n, p, x = self.right._display_aux()
			s = '%s' % self.key
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = self.left._display_aux()
		right, m, q, y = self.right._display_aux()
		s = '%s' % self.key
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2





"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, added size field  
	"""

	def __init__(self):
		self.root = None
		self.size = 0	#size is amount of nodes

	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key):
		if key == None: # key of virtual node
			return None
		node = self.root
		while node.key != None:
			if node.get_key() == key: # found
				return node
			elif key < node.get_key(): # go left
				node = node.get_left()
			else: # go right
				node = node.get_right()
		# if we finish the loop - key wasn't found
		return None


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		node = AVLNode(key,val) # initiate node
		# initialize virtal sons
		node.set_left(AVLNode(None, None))
		node.get_left().set_parent(node)
		node.set_right(AVLNode(None, None))
		node.get_right().set_parent(node)

		self.insertBST(node) # inserts node to BST tree
		self.size += 1
		blanceOps = self.rebalancing(node.get_parent(), "insert") # returns amount of ops
		return blanceOps

		
	def insertBST(self, node):
		# if tree is empty
		if self.root == None:
			self.root = node
		else: # find the parent of new node
			key = node.get_key()
			currNode = self.root
			while currNode.is_real_node():
				if key < currNode.get_key():
					currNode = currNode.get_left()
				else: # go right
					currNode = currNode.get_right()	
			parent = currNode.get_parent()
			# we updated the parent - now insert node as child
			node.set_parent(parent)
			if key < parent.get_key():
				parent.set_left(node)
			else:
				parent.set_right(node)
		# update height to zero and add 2 virtual sons		
		node.set_height(0)
		return


	def rebalancing(self, parent, case):
		# need to change delete so that it will not have a loop - just call rebalance
		cnt = 0
		while parent != None:
			bf = parent.get_BF()
			heightBefore = parent.get_height()
			heightAfter = parent.calculate_height()
			if abs(bf) < 2:
				if heightBefore == heightAfter:
					return cnt
				else:
					parent.set_height(heightAfter)
					parent = parent.get_parent()
					cnt += 1

			else:
				if bf == 2:
					left_child = parent.get_left()
					if left_child.get_BF() != -1:
						self.right_rotation(left_child, parent)
						cnt += 1
					else:
						self.left_rotation(left_child.get_right(), left_child)
						self.right_rotation(parent.get_left(), parent)
						cnt += 2

					# check which case we are in
					if case == "insert" or case == "join":
						return cnt
					else:# case == "delete" then move up the tree
						parent = parent.get_parent()	

				else: # BF == -2
					right_child = parent.get_right()
					if right_child.get_BF() != 1:
						self.left_rotation(right_child, parent)
						cnt += 1
						if case == "insert":
							return cnt
						else: # case == "delete" or case == "join" (join acts like delete) then move up the tree
							parent = parent.get_parent()

					else:
						self.right_rotation(right_child.get_left(), right_child)
						self.left_rotation(parent.get_right(), parent)
						cnt += 2
						# check which case we are in
						if case == "insert" or case == "join":
							return cnt
						else:# case == "delete" then move up the tree
							parent = parent.get_parent()	

				# we finished the loop (|root.get_BF()| == 2) and we didn't return
				return cnt
					
				
	

	def right_rotation(self, A, B):
		B.set_left(A.get_right())
		B.get_left().set_parent(B)
		A.set_right(B)
		A.set_parent(B.get_parent())
		if B.get_parent() == None: # B was a root - we need to make A the root
			self.root = A
		elif B.is_left_child():
			A.get_parent().set_left(A)
		else:
			A.get_parent().set_right(A)
		B.set_parent(A)

		newHeightB = B.calculate_height()
		if B.get_height() != B.calculate_height():
			B.set_height(newHeightB)
		
		newHeightA = A.calculate_height()
		if A.get_height() != A.calculate_height():
			A.set_height(newHeightA)

		

	def left_rotation(self, A, B):
		B.set_right(A.get_left())
		B.get_right().set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent())
		if B.get_parent() == None: # B was a root - we need to make A the root
			self.root = A		
		elif B.is_left_child():
			A.get_parent().set_left(A) #A and B have same parent
		else:
			A.get_parent().set_right(A)
		B.set_parent(A)

		#calculate new hieghts if necessarry - bottom up (B then A)
		newHeightB = B.calculate_height()
		if B.get_height() != B.calculate_height():
			B.set_height(newHeightB)
			
		newHeightA = A.calculate_height()
		if A.get_height() != A.calculate_height():
			A.set_height(newHeightA)


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		parent = self.deleteBST(node)
		balanceOps = 0
		balanceOps += self.rebalancing(parent, "delete")
		self.size -= 1
		return balanceOps

		
	def deleteBST(self, node):
		node_is_left = node.is_left_child() # check if node is left child (if not - then right child or root)
		is_root = (node.get_parent() == None)
		finalParent = node.get_parent()

		if node.get_height == 0:
			# simply remove leaf and pointers to and from it
			# check if leaf is left or right child
			if node_is_left():
				node.get_parent().set_left(None)
				node.set_parent(None)
			else:
				if is_root: # tree has only root
					self.root = None
				else:
					node.get_parent().set_right(None)
					node.set_parent(None)
		
		# node has only left child
		elif node.get_left().get_key() != None and node.get_right().get_key() == None:
			if is_root: # node is root
				self.root = node.get_left()
			elif node_is_left:
				node.get_parent().set_left(node.get_left())
			else: # is right child
				node.get_parent().set_right(node.get_left())
			
			node.get_left().set_parent(node.get_parent())

			node.set_left(None)
			node.set_parent(None)
			return finalParent
		
		# node has only right child
		elif node.get_left().get_key() == None and node.get_right().get_key() != None:
			if is_root: # node is root
				self.root = node.get_right()			
			elif node_is_left:
				node.get_parent.set_left(node.get_right())
			else: # is right child
				node.get_parent.set_right(node.get_right())

			node.get_right().set_parent(node.get_parent())

			node.set_right(None)
			node.set_parent(None)
			return finalParent
		
		# node has 2 children
		else: 
			suc = self.successor(node)
			finalParent = suc.get_parent()
			self.deleteBST(suc)

			#connect succesort to node posision
			suc.set_right(node.get_right())
			node.get_right().set_parent(suc)

			suc.set_left(node.get_left())
			node.get_left().set_parent(suc)
		
			suc.set_parent(node.get_parent())
			if is_root:
				self.root = node
			if node_is_left:
				suc.get_parent().set_left(suc)
			else:
				suc.get_parent().set_right(suc)

			#delete old node
			node.set_left(None)
			node.set_right(None)
			node.set_parent(None)

		#returns the parent of the physically deleted node (parent of leaf or successor)
		return finalParent			

		
	def successor(self, node):
		x = node.get_right()
		if x.is_real_node():
			# go as much left as possible
			while x.get_left().is_real_node():
				x = x.get_left()
			return x
		else: # go up left and stop on the first right or at root
			y = x.get_parent()
			while y != None and x == y.get_right():
				x = y
				y = x.get_parent()
			return y
			

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		stack = []
		sortedArray = []
		curr = self.root
		while curr.is_real_node() or stack.length == 0:
			while curr.is_real_node():
				stack.append(curr)
				curr = curr.get_left()
			curr = stack.pop() # pops minimum in stack
			sortedArray.append[(curr.get_key, curr.get_value)]
			curr = curr.get_right()
		return sortedArray

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.size
	
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		# what happens if one of node's children is virtual???
		# initiate left and right trees with elft and right children of node as root
		left = AVLTree()
		left.root = node.get_left()
		right = AVLTree()
		right.root = node.get_right()

		currNode = node
		while currNode.get_parent() != None:
			x = currNode.get_parent
			if currNode.is_left_child():
				newRight = AVLTree()
				newRight.root = x.get_right()
				right.join(newRight, x.get_key(), x.get_value())
				currNode = right.root # we assume that the parent of the new root is still the original parent
				# right is the corret pointer for right tree
			else: #currNode is right child - we need to join new subtree to left
				newLeft = AVLTree()
				newLeft.root = x.get_left()
				newLeft.join(left, x.get_key(), x.get_value())
				left = newLeft
				currNode = left.root

		return [left, right]

	
	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val):
		x = AVLNode(key, val)
		h1 = self.root.get_height()
		h2 = tree2.root.get_height()
		# joining the 2 trees makes legal AVL Tree
		if abs(h1 - h2) <= 1:
			a = self.root
			b = tree2.root
			c = None
		
		else:
			# tree2 is bigger than self
			if  h1 < h2 - 1:
				a = self.root
				a.set_parent(x)
				x.set_left(a)

				curr = tree2.root
				while curr.get_height >= h1 + 1:
					curr = curr.get_left()

				b = curr
				c = curr.get_parent()
				b.set_parent(x)
				c.set_left(x)
				x.set_right(b)
				# update root of joined tree
				self.root = tree2.root

			# self is bigger than tree2
			else:
				b = tree2.root
				b.set_parent(x)
				x.set_right(b)

				curr = self.root
				while curr.get_height >= h2 + 1:
					curr = curr.get_right()

				a = curr
				c = curr.get_parent()
				a.set_parent(x)
				c.set_right(x)
				x.set_left(a)
				# root doesn't change

		# update size of self
		self.size += tree2.size + 1

		# rebalnce if needed
		self.rebalancing(c, "join")

		return abs(h1 - h2) + 1


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
	
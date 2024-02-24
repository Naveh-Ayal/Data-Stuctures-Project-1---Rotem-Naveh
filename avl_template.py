
#id1       - 211698824
#name1     - Rotem Kerem
#username1 - Rotemkerem

#id2       - 209207638
#name2     - Naveh Ayal 
#username2 - Navehayal


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		# no additional fields added
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


	"""calculates the height of node

	@rtype: int
	@returns: height of self, calculated through the max hright of the children + 1
	"""
	
	def calculate_height(self):
		hLeft = self.left.height #height of left child
		hRight = self.right.height #height of right child
		return max(hLeft, hRight) + 1
	
	
	"""calculates the Balance Factor of node
	
	@rtype: int
	@returns: balance factor of self, calculated through sons' heights (left - right)
	"""
	def get_BF(self):
		return self.left.height - self.right.height 


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if (self.key == None) or (self == None):
			return False
		return True
	
	"""returns whether node is left child (if not - then right child)
	
	@rtype: bool
	@returns: True if self is left child, False if right or root.
	"""
	def is_left_child(self):
		if self.parent == None :
			return False
		if self.parent.left == self:
			return True
		return False



"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor,
	added field: .size
	"""

	def __init__(self):
		self.root = None
		self.size = 0	#size: mount of nodes in the tree



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
		while node.get_key() != None: # not a virtual node
			if node.get_key() == key: # found
				return node
			elif key < node.get_key(): # go left
				node = node.get_left()
			else: # go right
				node = node.get_right()
		# if loop finished - key wasn't found in tree
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
		 # initiate node
		node = AVLNode(key,val)

		# initialize 2 virtual sons
		leftVirtual = AVLNode(None, None)
		node.set_left(leftVirtual)
		leftVirtual.set_parent(node)

		rightVirtual = AVLNode(None, None)
		node.set_right(rightVirtual)
		rightVirtual.set_parent(node)

		# insert node to BST tree
		self.insertBST(node) 
		self.size += 1

		# rebalance the tree - make it AVL
		blanceOps = self.rebalancing(node.get_parent(), "insert")

		# return amount of balance operations
		return blanceOps
	


	"""inserts node to BST

	@type node: AVLNode
	@pre: node.key currently does not appear in the dictionary
	@rtype: None
	"""
		
	def insertBST(self, node):
		# if tree is empty update root
		if self.root == None:
			self.root = node
		else: # find the parent of new node
			key = node.get_key()
			currNode = self.root
			parent = currNode.get_parent()
			while currNode.is_real_node(): #binary search
				parent = currNode
				if key < currNode.get_key(): # go left
					currNode = currNode.get_left()
				else: # go right
					currNode = currNode.get_right()	
					
			# we updated the parent - now insert node as child
			node.set_parent(parent)
			if key < parent.get_key():
				parent.set_left(node)
			else:
				parent.set_right(node)

		# update height to zero 	
		node.set_height(0)
		return
	
	

	"""rebalances BST to AVLTree

	@type node: AVLNode
	@pre: node in dictionary
	@type case: str
	@pre: one of 3 cases - "insert", "delete", "join"
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def rebalancing(self, node, case):
		# optional cases: "insert", "delete", "join"
		cnt = 0 #restart num of operations
		while node != None: # not at the root
			bf = node.get_BF()
			heightBefore = node.get_height()
			heightAfter = node.calculate_height()
			#divide into cases:
			if abs(bf) < 2:
				if heightBefore == heightAfter: #all good
					return cnt
				else: #update height
					node.set_height(heightAfter)
					node = node.get_parent()
					cnt += 1

			else:
				if bf == 2:
					left_child = node.get_left()
					if left_child.get_BF() != -1:
						self.right_rotation(left_child, node)
						cnt += 1
					else:
						self.left_rotation(left_child.get_right(), left_child)
						self.right_rotation(node.get_left(), node)
						cnt += 2

					# check which case we are in
					if case == "insert" or case == "join":
						return cnt
					else:# case == "delete" then move up the tree
						node = node.get_parent()	

				else: # BF == -2
					right_child = node.get_right()
					if right_child.get_BF() != 1:
						self.left_rotation(right_child, node)
						cnt += 1
						# check which case we are in
						if case == "insert":
							return cnt
						else: # case == "delete" or case == "join" (join acts like delete) then move up the tree
							node = node.get_parent()

					else:
						self.right_rotation(right_child.get_left(), right_child)
						self.left_rotation(node.get_right(), node)
						cnt += 2
						# check which case we are in
						if case == "insert" or case == "join":
							return cnt
						else:# case == "delete" then move up the tree
							node = node.get_parent()	

				# we finished the loop (|root.get_BF()| == 2) and we didn't return
				return cnt
					
	"""performs right rotation in BST

	@type A: AVLNode
	@pre: node in dictionary
	@type B: AVLNode
	@pre: node in dictionary
	@rtype: None
	"""			
	
	def right_rotation(self, A, B):
		# switching A with B:
		B.set_left(A.get_right())
		B.get_left().set_parent(B)
		A.set_right(B)
		A.set_parent(B.get_parent())
		#connect up the tree:
		if B.get_parent() == None: # B was a root - we need to make A the root
			self.root = A
		elif B.is_left_child():
			A.get_parent().set_left(A)
		else: #B is right child
			A.get_parent().set_right(A)
		B.set_parent(A)
		#calculate new heights if necessarry - bottom up (B then A)
		newHeightB = B.calculate_height()
		if B.get_height() != B.calculate_height():
			B.set_height(newHeightB)
		
		newHeightA = A.calculate_height()
		if A.get_height() != A.calculate_height():
			A.set_height(newHeightA)

	
	"""performs left rotation in BST

	@type A: AVLNode
	@pre: node in dictionary
	@type B: AVLNode
	@pre: node in dictionary
	@rtype: None
	"""		

	def left_rotation(self, A, B):
		# switching a with b:
		B.set_right(A.get_left())
		B.get_right().set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent())
		#connect up the tree:
		if B.get_parent() == None: # B was a root - we need to make A the root
			self.root = A		
		elif B.is_left_child():
			A.get_parent().set_left(A) #A and B have same parent
		else:#B is right child
			A.get_parent().set_right(A)
		B.set_parent(A)

		#calculate new heights if necessarry - bottom up (B then A)
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
		parent = self.deleteBST(node) # deletes node and returns parent of deleted node
		balanceOps = 0 
		balanceOps += self.rebalancing(parent, "delete") # maintains AVL, returns num actions
		self.size -= 1
		return balanceOps

	"""deletes node from BST

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: AVLNode
	@returns: parent of node that was effectively deleted
	"""	
	def deleteBST(self, node):
		node_is_left = node.is_left_child() # check if node is left child (if not - then right child or root)
		is_root = (node.get_parent() == None) # check if node is root
		finalParent = node.get_parent()

		if node.get_height() == 0:
			# simply remove leaf and pointers to and from it
			# check if leaf is left or right child and add virtual child accordingly
			if node_is_left:
				node.get_parent().set_left(AVLNode(None, None))
				node.set_parent(None)
			else:
				if is_root: # tree has only root
					self.root = None
				else:
					node.get_parent().set_right(AVLNode(None, None))
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
				node.get_parent().set_left(node.get_right())
			else: # is right child
				node.get_parent().set_right(node.get_right())
			
			node.get_right().set_parent(node.get_parent())

			#delete all connections of the node
			node.set_right(None)
			node.set_parent(None)
			return finalParent
		
		# node has 2 children
		else: # switch with the successor and delete node at the successor place
			suc = self.successor(node) # find successor
			finalParent = suc.get_parent() #remember the start point for rebalancing
			self.deleteBST(suc) # delete successor

			#connect succesor to node posision (replacing the node)
			suc.set_right(node.get_right())
			node.get_right().set_parent(suc)

			suc.set_left(node.get_left())
			node.get_left().set_parent(suc)
		
			suc.set_parent(node.get_parent())
			
			if is_root: #if node was root- connect to the tree
				self.root = suc
			elif node_is_left:
				suc.get_parent().set_left(suc)
			else:
				suc.get_parent().set_right(suc)

			#delete old node
			node.set_left(None)
			node.set_right(None)
			node.set_parent(None)

		#returns the parent of the physically deleted node (parent of leaf or successor)
		return finalParent			

	"""finds the successor of given node

	@type node: AVLNode
	@pre: node in dictionary
	@rtype: AVLNode
	@returns: successor of node in the tree, none if it's maximum
	"""		

	def successor(self, node):
		x = node.get_right()
		if x.is_real_node(): # if node have right child
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
		stack = [] #saves sizes and pointers as we go down, thus we dont need to go back up
		sortedArray = []
		curr = self.root
		while curr.is_real_node() or len(stack) != 0:
			while curr.is_real_node(): #we can go down
				stack.append(curr) #remember where we have been
				curr = curr.get_left()
			curr = stack.pop() # pops minimum in stack
			sortedArray.append((curr.get_key(), curr.get_value()))
			curr = curr.get_right() #continue going down if possible (real node), if not, continue poping (resemble going up)
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
		# initiate left and right trees
		# left and right children of node as roots
		left = AVLTree()
		if  node.get_left().is_real_node(): # if node has smaller child
			left.root = node.get_left()
		#else: left stays empty
		right = AVLTree()
		if  node.get_right().is_real_node():#if node has larger child
			right.root = node.get_right()
		#else: right stays empty
		
		if node == self.root: #no spliting to do
			return [left, right]
		
		#else: node is not root
		grandpa = node.get_parent().get_parent() # pointer for parent of parent of node in original tree
		parent = node.get_parent()
		parent_is_left = parent.is_left_child() #remember for the next iteration
		child = node
		child_is_left = child.is_left_child()
		while parent != None: #not at the root (the end)
			if child_is_left:
				newRight = AVLTree()
				if parent.get_right().is_real_node(): #if parent has larger children
					newRight.root = parent.get_right()
					newRight.root.set_parent(None) # cutting the new tree from original 
				# if parent.right is vitual node - newLeft stays empty

				right.join(newRight, parent.get_key(), parent.get_value())
				# right is the corret pointer for right tree

			else: #currNode is right child - we need to join new subtree to left
				newLeft = AVLTree()
				if parent.get_left().is_real_node():#if parent has smaller children
					newLeft.root = parent.get_left()
					newLeft.root.set_parent(None) # cutting the new tree from original 
				# if parent.left is virtual node - newLeft stays empty

				newLeft.join(left, parent.get_key(), parent.get_value())
				left = newLeft #keeping the right pointers and values

			# move up the original tree
			child_is_left = parent_is_left 
			parent = grandpa
			if parent != None: 
				parent_is_left = grandpa.is_left_child()
				grandpa = grandpa.get_parent()
		
		# return list with both trees
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
		# empty tree cases - insert x
		if self.root == None or tree2.root == None:
			if self.root != None:
				h = self.root.calculate_height() + 1
				self.insert(x.get_key(),x.get_value())
			elif tree2.root != None:
				h = tree2.root.calaculate_height() + 1
				tree2.insert(x.get_key(),x.get_value())
				self.root = tree2.root
			else:
				h = 0
				self.insert(x.get_key(),x.get_value()) # inserts x as root with 2 virtual sons

			# update size of self
			self.size += tree2.size
			return h + 1
		
		# both trees are not empty
		h1 = self.root.get_height()
		h2 = tree2.root.get_height()
		
		if abs(h1 - h2) <= 1: # joined trees make legal AVL Tree
			# a will be root of left subtree
			a = self.root
			x.set_left(a)
			a.set_parent(x)

			# b will be root of right subtree
			b = tree2.root
			x.set_right(b)
			b.set_parent(x)

			# c will be where we start rebalancing 
			c = None

			# x will be temporary root
			self.root = x
			self.root.set_height(self.root.calculate_height())
		
		else:
			if  h1 < h2 - 1: # tree2 is bigger than self
				# self stays whole
				a = self.root
				a.set_parent(x)
				x.set_left(a)

				# travel down tree2 to find root of new subtree
				curr = tree2.root
				while curr.get_height() >= h1 + 1: #go left
					curr = curr.get_left()

				# update pointers
				b = curr
				c = curr.get_parent()
				b.set_parent(x)
				c.set_left(x)
				x.set_right(b)

				# update root of joined tree
				self.root = tree2.root
				self.root.set_parent(None)

			else: # self is bigger than tree2
				# tree2 stays whole
				b = tree2.root
				b.set_parent(x)
				x.set_right(b)

				# travel down self to find root of new subtree
				curr = self.root
				while curr.get_height() >= h2 + 1:
					curr = curr.get_right()

				# update pointers
				a = curr
				c = curr.get_parent()
				a.set_parent(x)
				c.set_right(x)
				x.set_left(a)
				# root doesn't change

			# rebalnce if needed
			self.rebalancing(c, "join")

		# update size of self
		self.size += tree2.size + 1

		# return runtime - difference in height + 1
		return abs(h1 - h2) + 1


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
	

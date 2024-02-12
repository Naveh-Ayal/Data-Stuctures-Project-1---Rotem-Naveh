#username - rotemNaveh
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
		# add size later
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	# returns left son - if leaf or virtual - will return None
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


	"""calculates the height of the node"""
	def calculate_height(self):
		hLeft = self.left.height #height of left child
		hRight = self.right.height #height of right child
		return max(hLeft, hRight) + 1
	
	
	"""calculates the Balance Facror of the node"""
	def get_BF(self):
		return self.left.height - self.right.height 


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if (self.key == None) return False
		return True
	
	"""returns whether self node is left child (if not - then right child)"""
	def is_left_child(self):
		if self.parent.left == self:
			return True
		return False

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# add your fields here

	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key):
		if key == None:
			return None
		node = self.root
		while node.key != None:
			if node.get_key() == key:
				return node
			elif key < node.get_key():
				node = node.get_left()
			else:
				node = node.get_right()
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
		node = AVLNode(key,val)
		self.inserBST(node)
		parent = node.get_parent
		blanceOps = self.rebalancing(parent)
		return blanceOps


	def rebalancing(self, parent):
		while parent != None:
			bf = parent.get_BF()
			heightBefore = parent.get_height()
			heightAfter = parent.calculate_height()
			if abs(bf) < 2:
				if heightBefore == heightAfter:
					return 0
				else:
					parent.set_height(heightAfter)
					parent = parent.get_parent()
			else:
				if bf == 2:
					left_child = parent.get_left()
					if left_child.get_BF() != -1:
						self.right_rotation(left_child, parent)
						return 1
					else:
						self.left_rotation(left_child.get_right(), left_child)
						self.right_rotation(parent.get_left(), parent)
						return 2
				else:
					right_child = parent.get_right()
					if right_child.get_BF() != 1:
						self.left_rotation(right_child, parent)
						return 1
					else:
						self.right_rotation(right_child.get_left(), right_child)
						self.left_rotation(parent.get_right(), parent)
						return 2


					
				
	

	def right_rotation(self, A, B):
		B.set_left(A.get_right)
		B.get_left.set_parent(B)
		A.set_right(B)
		A.set_parent(B.get_parent)
		if self.is_left_child(A):
			A.get_parent.set_left(A)
		else:
			A.get_parent.set_right(A)
		B.set_parent(A)



	def left_rotation(self, A, B):
		B.set_right(A.get_left)
		B.get_right.set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent)
		if self.is_left_child(A):
			A.get_parent.set_left(A)
		else:
			A.get_parent.set_right(A)
		B.set_parent(A)
		
		newHeightA = A.calculate_height
		if A.get_height() != A.calculate_height:
			A.set_height(newHeightA)

		newHeightB = B.calculate_height
		if B.get_height() != B.calculate_height:
			B.set_height(newHeightB)
				

			
			



	
	
	def insertBST(self, node):
		if self.root == None:
			self.root = node
			return
		key = node.get_key
		parent = self.findParent(self.root, key)
		node.set_parent(parent)
		if key < parent.get_key():
			parent.set_left(node)
		else:
			parent.set_right(node)
		node.set_height(0)
		return

	def findParent(root, key):
		currNode = root
		while currNode != None:
			if key < currNode.key:
				currNode = currNode.left
			else:
				currNode = currNode.right
			
		return currNode.parent






	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return -1	

	
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
		return None

	
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
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return None
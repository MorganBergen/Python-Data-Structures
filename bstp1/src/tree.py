
from typing_extensions import runtime
from node import Node

class Tree:
	
	def __init__(self):
		self.root = None
		self.size = 0
	
	# visit, left, right
	def preorder(self, subtree):
		print(subtree.key)
		self.preorder(subtree.left)
		self.preorder(subtree.right)
	
	# left, visit, right
	def inorder(self, subtree):
		self.inorder(subtree.left)
		print(subtree.key)
		self.inorder(subtree.right)
		
	# left, right, visit
	def postorder(self, subtree):
		self.postorder(subtree.left)
		self.postorder(subtree.right)
		print(subtree.key)
		
	def __contains__(self, key):
		return (self._search(self.root, key) != None)

	def valueOf(self, key):
		node = self._search(self.root, key)
		if node == None:
			print("invalid key")
		else:
			return (node.data)
		
	
	# adds a new entry to the tree or replaces the value of an existing one
	def add(self, key, data):
	
		# find the node containing the key, if it exists
		node = self._search(self.root, key)
		
		#if the key is already in the tree, updates its value
		if node == None and self.root == None:
			self.root = Node(key, data)

		# otherwise add a new entry
		else:
			self.root = self._insert(self.root, key, data)
			self.size += 1
			return True
			
	
	def _insert(self, subtree, key, data):
		if subtree == None:
			subtree = Node(key, data)
		elif key < subtree.key:
			subtree.left = self._insert(subtree.left, key, data)
		elif key > subtree.key:
			subtree.right = self._insert(subtree.right, key, data)
		return subtree
	
	
	
	
	def _search(self, subtree, target_key):
		
		# base case for the root being none
		if subtree == None:
			return None
		
		# target is left of the subtree root
		elif target_key < subtree.key:
			if subtree.left == None:
				return subtree
			else:
				return self._search(subtree.left, target_key)
		
		# target is right of the subtree root
		elif target_key > subtree.key:
			if subtree.right == None:
				return subtree
			else:
				return self._search(subtree.right, target_key)
				
		
		# base case
		# the target is contained in the current node
		# returns a reference to the current node containing that key
		else:
			return subtree
			
	
		
	def _min(self, subtree):
		if subtree == None:
			return None
		elif subtree.left == None:
			return subtree
		else:
			return (self._min(subtree.left))

	def _max(self, subtree):
		if subtree == None:
			return None
		elif subtree.right == None:
			return subtree
		else:
			return (self._max(subtree.right))
			
	
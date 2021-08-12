# -*- coding: utf-8 -*-
# 基础二叉树Python实现

class Node:  # 节点结构
	def __init__(self):
		self.item = None  # 节点保存项目
		self.left = None  # 节点中包含的左节点
		self.right = None  # 节点中包含的右节点


class Pair:  # 遍历二叉树时需要用到的结构
	def __init__(self):
		self.parent = None  # 结构成员
		self.child = None  # 结构成员


class CreateTree:  # 二叉树结构实例
	def __init__(self, maxitems=10):  # 初始化函数,默认最大节点数为10
		self.__root = None  # 二叉树根节点
		self.__size = 0  # 二叉树节点数
		self.maxitems = maxitems  # 可包含最大节点数

	def TreeIsEmpty(self):  # 二叉树接口函数,检查树是否为空
		if self.__root is None:
			print('Tree is empty.')
			return 1
		else:
			print('Tree is not empty.')
			return 0

	def TreeIsFull(self):  # 二叉树接口函数,检查树是否已满
		if self.__size == self.maxitems:
			print('Tree is full!')
			return 1
		else:
			return 0

	def TreeItemCount(self):  # 检查二叉树包含的节点数
		print('当前节点数:', self.__size)
		return self.__size

	def AddItem(self, **item):  # 二叉树重要接口函数,为树添加项目,请注意传入参数格式
		if self.TreeIsFull():  # 先判断树是否已满,如果已满返回False.
			return 0
		elif self.__SeekItem(item).child is not None:	# 使用__SeekItem函数检查树中是否有重复项目,如有返回false
			print('Attempted to add duplicate item')
			return 0
		else:  # 树中有空位且项目不重复则在树中新建节点并存入项目
			node = Node()  # 使用Node类初始化一个节点
			node.item = item  # 将新增项目存入新建的节点中
			self.__size += 1  # 二叉树节点数+1
			if self.__root is None:  # 若根节点为空,把根节点设为新节点
				self.__root = node
				print('成功创建根节点!')
			else:  # 若根节点不为空,以新建的节点为参数传入__AddNode函数,使新增的节点加入二叉树
				self.__AddNode(node, self.__root)  # node为参数调用__AddNode接口函数

	def InTree(self, item):  # 用户接口函数,使用__SeekItem函数判断树中项目是否存在
		if not isinstance(item, dict):  # 判读参数传入格式,项目以字典格式保存
			print('请输入字典格式!')
		else:
			if self.__SeekItem(item).child is None:  # 调用__SeekItem函数判读
				print('此项目不在树中!')
				return 0
			else:
				print('树中含有此项目!')
				return 1

	def __DeleteNode(self, node):  # 私有,删除节点函数,二叉树重要接口函数,传入节点对象参数
		print('Try delete:', node.item)  # 输出信息
		if node.left is None:  # 判断需要删除节点的左子树是否为空,为空则将当前节点右子树变为当前节点
			node = node.right
			self.__size -= 1
			return 1
		elif node.right is None:  # 判断需要删除节点右子树是否为空,为空则将当前节点左子树变为当前节点
			node = node.left
			self.__size -= 1
			return 1
		else:  # 若左右子树都不为空,则把左子树变为当前节点,把右子树加到左子树的最后(叶节点)
			temp = node.left
			while temp.right is not None:
				temp = temp.right
			temp.right = node.right
			node = node.left
			self.__size -= 1
			return 1

	def DeleteItem(self, item):  # 删除项目函数,调用__DeleteNode函数实现
		if not isinstance(item, dict):  # 检查项目传入格式,应为字典格式
			print('请输入字典格式!')
		else:  # 格式检查通过后执行
			look = self.__SeekItem(item)  # 执行__SeekItem函数查找需要删除项目所在的节点
			if look.child is None:  # 未找到项目存在的节点,树中不包含该项目,提前返回false
				print('树中无此项目')
				return 0
			if look.parent is None:  # 若找到所需要删除项目位置为根节点,则删除根节点
				if self.__DeleteNode(self.__root):
					print('删除成功')
					return 1
			elif look.parent.left == look.child:  # 找到项目位于父节点中的左子树,操作删除父节点的左子树
				if self.__DeleteNode(look.parent.left):
					print('删除成功')
					return 1
			else:
				if self.__DeleteNode(look.parent.right):  # 若前几项都不满足,则处于父节点右子树,操作删除之
					print('删除成功')
					return 1


	def DeleteAll(self):  # 用户接口函数,清空二叉树,调用__DeleteAllNodes函数实现
		if self.__root is not None:
			self.__DeleteAllNodes(self.__root)

	def __DeleteAllNodes(self, root):  # 删除以传入节点为根节点的所有节点,为递归函数,从根节点开始,递归向下,同理遍历函数
		if root is not None:
			pright = root.right
			self.__DeleteAllNodes(root.left)
			root = None
			self.__DeleteAllNodes(pright)

	def __SeekItem(self, item):  # 私有,重要函数,寻找项目所在节点,调用__Toleft/__Toright函数判断左右
		look = Pair()  # 初始化寻找实例
		look.child = self.__root
		if look.child is None:
			return look
		while look.child is not None:
			if self.__Toleft(item, look.child.item):
				look.parent = look.child
				look.child = look.child.left
			elif self.__ToRight(item, look.child.item):
				look.parent = look.child
				look.child = look.child.right
			else:
				break
		return look

	def __AddNode(self, node, root):  # 私有,添加节点函数,为递归函数,需要传入所需添加的节点和其应所在位置的父节点两个参数
		if self.__Toleft(node.item, root.item):  # 判断存在父节点的左子树中
			if root.left is None:  # 若父节点中左子树为空则添加之
				root.left = node
				print('节点添加成功!')
				print(node.item)
			else:
				self.__AddNode(node, root.left)  # 否则递归调用在父节点左子树中寻找空位
		elif self.__ToRight(node.item, root.item):  # 判断位置为父节点右子树,原理同上
			if root.right is None:
				root.right = node
				print('节点添加成功!')
				print(node.item)
			else:
				self.__AddNode(node, root.right)
		else:
			print('节点添加失败!')
			return 0

	def __Toleft(self, item1, item2):  # 私有,判断项目进入二叉树后的左去向,二叉树核心算法,可根据需求修改
		item2_values = *item2.values(),
		item1_values = *item1.values(),
		if (com1 := self.__strcmp(item1_values[0], item2_values[0])) < 0:
			return 1
		elif com1 > 0:
			return 0
		else:
			item2_keys = *item2.keys(),
			item1_keys = *item1.keys(),
			i = 0
			while com1 == 0:
				try:
					com1 = self.__strcmp(item1_keys[i], item2_keys[i])
					if com1 < 0:
						return 1
					if com1 > 0:
						return 0
					i += 1
					com1 = self.__strcmp(item1_values[i], item2_values[i])
					if com1 < 0:
						return 1
					if com1 > 0:
						return 0
				except BaseException:
					return 0

	def __ToRight(self, item1, item2):  # 私有,判断项目进入二叉树后的左去向,二叉树核心算法,可根据需求修改
		item2_values = *item2.values(),
		item1_values = *item1.values(),
		if (com1 := self.__strcmp(item1_values[0], item2_values[0])) > 0:
			return 1
		elif com1 < 0:
			return 0
		else:
			item2_keys = *item2.keys(),
			item1_keys = *item1.keys(),
			i = 0
			while com1 == 0:
				try:
					com1 = self.__strcmp(item1_keys[i], item2_keys[i])
					if com1 > 0:
						return 1
					if com1 < 0:
						return 0
					i += 1
					com1 = self.__strcmp(item1_values[i], item2_values[i])
					if com1 > 0:
						return 1
					if com1 < 0:
						return 0
				except BaseException:
					return 0

	def EmptyTree(self):  # 清空树,调用DeleteAll函数
		self.DeleteAll()

	def Traverse(self):  # 遍历二叉树,调用下方__InOrder函数
		print('二叉树遍历:')
		self.__InOrder(self.__root)

	def __InOrder(self, root):  # 私有,遍历函数的实现函数,为递归函数,原理与删除节点相同
		if root is not None:
			print(root.item)
			self.__InOrder(root.left)
			self.__InOrder(root.right)

	def Search(self, item):  # 首键值搜索
		print('Search item:', item)
		print('Result:')
		look = Pair()  # 初始化寻找实例
		look.child = self.__root
		if look.child is None:
			print('此树为空树,请添加项目')
			return 0
		while look.child is not None:
			if self.__Toleft(item, look.child.item):
				look.parent = look.child
				look.child = look.child.left
			elif self.__ToRight(item, look.child.item):
				look.parent = look.child
				look.child = look.child.right
			else:
				print(look.child.item)
				break

	def __strcmp(self, str1, str2):  # 私有,比较项目函数
		str1 = str(str1)
		str2 = str(str2)
		if str1 < str2:
			return -1
		if str1 == str2:
			return 0
		if str1 > str2:
			return 1


if __name__ == '__main__':
	Tree = CreateTree()  # 初始化二叉树类实例
	Tree.AddItem(a=9, b=2)
	Tree.AddItem(name=8, age=10)	# 添加项目
	Tree.AddItem(name=8, age=10)
	Tree.AddItem(name=7, age=10)
	Tree.AddItem(a=7)
	Tree.Traverse()	# 遍历二叉树项目
	Tree.Search({'a': 9})	# 搜索项目

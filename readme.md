Simple binary tree by Python.

简单二叉树的Python实现

//function

//实现函数

​	TreeIsEmpty()

​	TreeIsFull()

​	TreeItemCount()

​	AddItem(**item)

​	InTree(item) //item is dict.  //item为字典格式

​	__DeleteNode(node)  #private   //node is object  //node为node对象

​	DeleteItem(item) //item is dict 

​	DeleteAll()

​	DeleteAllNodes(root) //root is node_object  //参数root为节点对象

​	__SeekItem(item)  #private   //item is dict



​	__AddNode(node,root)  #private   //node is a new object ,root is root node	//node为新增节点对象, 以root对象为根节点



​	__Toleft(item1,item2)  #private  //both item is dict  //item1 item2皆为dict字典



​	__ToRight(item1,item2) #private

​	EmptyTree()	#interface

​	Traverse()	#traverse interface  #遍历接口函数

​	__InOrder(root)	#private to traverse  #私有函数,遍历函数的实现

​	Search(item)  #search item   #搜索项目

​	__strcmp(str1,str2) #compare str  #比较字符串

​	

​	
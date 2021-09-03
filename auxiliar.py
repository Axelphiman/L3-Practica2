from nodo import Nodo


# auxiliar
def buildUtil(In, post, inStrt, inEnd, pIndex):
    # Caso base
    if (inStrt > inEnd):
        return None

    node = Nodo(post[pIndex[0]])
    pIndex[0] -= 1

    if (inStrt == inEnd):
        return node
    iIndex = search(In, inStrt, inEnd, node.data)

    node.right = buildUtil(In, post, iIndex + 1,
                           inEnd, pIndex)
    node.left = buildUtil(In, post, inStrt,
                          iIndex - 1, pIndex)
    return node


# construye arbol binario dados los arreglos inorden y postorden
def buildTree(In, post, n):
    pIndex = [n - 1]
    return buildUtil(In, post, 0, n - 1, pIndex)


# busqueda de la raiz en la serie inorder
def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value):
            break
    return i


# retorna el vector de nodos en orden postorder
def postOrderDirectionalNodeVector(root):
    s1 = []
    s2 = []
    result = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        node = s2.pop()
        result.append(node)
    return result


# Convierte arbol binario en arbol binario enNodo    queue = []
    head = binary_thread_tree_node(None, root, None, 1, 1)
    head.right = head
    p = root
    queue.append(p)
    for i in range(len(Vector)):
        if Vector[i].left is None:
            k = 0
            while Vector[k] != Vector[i]:
                k += 1
            Vector[i].left = Vector[k - 1]
            Vector[i].bi = 0
        else:
            Vector[i].bi = 1
        if Vector[i].right is None:
            k = 0
            while Vector[k] != Vector[i]:
                k += 1
            Vector[i].right = Vector[k + 1]
            Vector[i].bd = 0
        else:
            Vector[i].bd = 1

    return (root, head)


# Recorre un arbol enhebrado en post order
def postOrderThread(head, root):
    if root != head:
        if root.bi == 1: postOrderThread(head, root.left)
        if root.bd == 1: postOrderThread(head, root.right)
        print(root)


# Retorna una lista con las hojas del arbol dado su vector de nodos (En cualquier orden)
def leafsFromTree(VectorNodes):
    leafs = []
    for node in VectorNodes:
        if node.bi == 0 and node.bd == 0:
            leafs.append(node)
    return leafs


# Camino del camino desde la raiz hasta el dato k
def pathToNode(root, path, k):
    if root is None:
        return False

    path.append(root.data)
    if root.data == k:
        return True
    if ((root.bi == 1 and pathToNode(root.left, path, k)) or
            (root.bd == 1 and pathToNode(root.right, path, k))):
        return True
    path.pop()
    return False


# Se halla el minimo ancestro comun y con esta informacion se halla la distancia entre los datos 1 y 2
def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)
        path2 = []
        pathToNode(root, path2, data2)
        i = 0
        while i < len(path1) and i < len(path2):

            if path1[i] != path2[i]:
                break
            i = i + 1

        return (len(path1) + len(path2) - 2 * i)
    else:
        return 0


"""Guia para evaluar el ejercicio:

    Se deben modificar los arreglos In y Post con las respectivas
    series InOrden y PostOrden del arbol que se desea evaluar
    esta es la manera "interactiva" de ingresar arboles y testearlos

    PD: Estas series pueden ser numeros o caracteres
    """

In = [1, 2, 'B', 'I', 'H', 'G', 'A', 'C', 'E', 'D', 'F']
Post = [1, 2, 'I', 'G', 'H', 'B', 'E', 'F', 'D', 'C', 'A']
n = len(In)

root = buildTree(In, Post, n)
nodos = postOrderDirectionalNodeVector(root)
root, head = threadingBinaryTree(root, nodos)
print("Nodos en postOrder")
postOrderThread(head, root)
print("")
print("Hojas: ")
leafs = leafsFromTree(nodos)
print([leaf.data for leaf in leafs])
print("")
for dato1 in leafs:
    for dato2 in leafs:
        print("Distancia entre las hojas {} & {}: {}".format(dato1.data, dato2.data,
                                                             distance(root, dato1.data, dato2.data)))

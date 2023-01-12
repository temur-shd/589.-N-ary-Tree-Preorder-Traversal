# 589.-N-ary-Tree-Preorder-Traversal
589. N-ary Ağaç Ön Sipariş Geçişi


Bir n-ary ağacının kökü göz önüne alındığında, düğümlerinin değerlerinin ön sipariş geçişini döndürün.

Nary-Tree giriş serileştirmesi, seviye sırası geçişlerinde temsil edilir. Her çocuk grubu boş değerle ayrılır 

![image](https://user-images.githubusercontent.com/77336040/212171119-b99d411e-09eb-41a9-8ae1-c4f22ec1c5ef.png)


Deep-First-Search(DFC) mantığı kullanarak ilerlenir.
DFC adı üstünde derinliğin öncelik olduğu graph arama algoritmasıdır.
Bir root(kök) seçili ve herhangi bir alt node(düğüm)(children seçilerek) en uçtaki düğüme kadar gidir.
Düğümleri stack(yığın) mantığıyla tutar. (Yani LIFO(son giren ilk çıkar))
Her düğümün bir kez gezilme şartı olduğu için karmaşıklığı O(N)'dir.
-----------------------
Bu kodda da önce boş bir liste tanımlanır ve döngü ile düğümlerde ilerlenerek children düğüm değerleri yazılır. Boş ise null değer listeye eklenir.



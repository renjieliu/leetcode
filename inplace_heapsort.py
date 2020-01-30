def swap(arr, A, B):
  t = arr[A]
  arr[A] = arr[B]
  arr[B] = t

def heapify(arr, s, e):
  c1 = s*2+1
  c2 = c1+1
  maxx = s
  if c1 <= e and arr[c1] > arr[maxx]:
    maxx = c1
  if c2 <= e and arr[c2] > arr[maxx]:
    maxx = c2
  if maxx!=s:
    swap(arr, maxx, s)
    heapify(arr, maxx, e)

def build_heap(arr):
  s = ((len(arr)-1)-1 )//2
  while s > -1:
    heapify(arr, s, len(arr)-1)
    s-=1

def heap_sort(arr):
  build_heap(arr)
  s = len(arr)-1
  while s > -1:
    swap(arr, 0, s)
    heapify(arr, 0, s-1)
    s-=1

a = [2,42,34,1,4,2143,1]
heap_sort(a)
print(a)


package main

type Store[K comparable, V any] interface {
	Put(K, V) error
	Get(K) ([]V, error)
	Update(K, V) (K, V)
}

type KVStore[K comparable, V any] struct {
	data map[K]V
}

type Block struct {}
type Transaction struct {}

func NewKVStore[K comparable, V any]() *KVStore[K, V] {
	return &KVStore[K,V]{
		data : make(map[K]V),
	}
}


func main() {
	_  = NewKVStore[string, *Block]()
	_ = NewKVStore[string, *Transaction]()
}



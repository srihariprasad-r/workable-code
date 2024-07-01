package main

import "fmt"

type Store[K comparable, V any] interface {
	Put(K, V) error
	Get(K) ([]V, error)
	Update(K, V) (K, V)
}

type KVStore[K comparable, V any] struct {
	data map[K]V
}

type Block struct{}
type Transaction struct{}

func NewKVStore[K comparable, V any]() *KVStore[K, V] {
	return &KVStore[K, V]{
		data: make(map[K]V),
	}
}

func (s *KVStore[K, V]) Put(key K, value V) error {
	s.data[key] = value
	return nil
}

func (s *KVStore[K, V]) Get(key K) (V, error) {
	val, err := s.data[key]
	if !err {
		return val, fmt.Errorf("No key found")
	}
	return val, nil
}

func main() {
	//_  = NewKVStore[string, *Block]()
	//_ = NewKVStore[string, *Transaction]()
	//var c Store[string, string]
	store := NewKVStore[string, string]()
	store.Put("foo", "bar")

	fmt.Println(store.Get("foo"))
}

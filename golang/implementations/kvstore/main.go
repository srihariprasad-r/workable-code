package main

import (
	"fmt"
	"net/http"
)

type Store[K comparable, V any] interface {
	Put(K, V) error
	Get(K) (V, error)
	Update(K, V) (V, error)
}

type KVStore[K comparable, V any] struct {
	data map[K]V
}

type Server struct {
	store Store[string, string]
	ListenAddr string
}

type Block struct{}
type Transaction struct{}

func NewKVStore[K comparable, V any]() *KVStore[K, V] {
	return &KVStore[K, V]{
		data: make(map[K]V),
	}
}

func (s *KVStore[K, V]) Update(key K, value V) (V, error) {
	val, err := s.Get(key)
	if err == nil {
		s.data[key] = value
		fmt.Println("Old value for : " , key , " is " , val, "  which has been updated to: " , s.data[key])
		return val, nil
	} else {
		return val, err
	}
}

func (s *KVStore[K, V]) Put(key K, value V) error {
	s.data[key] = value
	fmt.Println(s.data)
	return nil
}

func (s *KVStore[K, V]) Get(key K) (V, error) {
	val, err := s.data[key]
	if !err {
		return val, fmt.Errorf("No key found")
	}
	return val, nil
}

func NewServer(address string) *Server {
	return &Server{
		store: NewKVStore[string, string](),
		ListenAddr: address,
	}
}

func (s *Server) Start() {
	http.ListenAndServe(s.ListenAddr, nil)
}

func main() {
	//_  = NewKVStore[string, *Block]()
	//_ = NewKVStore[string, *Transaction]()
	//var c Store[string, string]
	// store := NewKVStore[string, string]()
	// store.Put("foo", "bar")

	// fmt.Println(store.Get("foo"))

	s := Server {
		store: NewKVStore[string, string](),
	}

	s.store.Put("foo", "bar")
	fmt.Println(s.store.Get("foo"))
	// s := NewServer(":3000")
	// s.Start()
}

package main

import "fmt"

type Storer interface {
	Put([]byte) (int, error)
	Fetch(int) ([]byte, error)
}

type MemoryStore struct {
	data [][]byte
}

type StoredFunc func() Storer

func NewMemoryStore() *MemoryStore {
	return &MemoryStore{
		data: make([][]byte, 0),
	}
}

func (s *MemoryStore) Put(d []byte) (int, error) {
	s.data = append(s.data, d)
	return len(s.data) - 1, nil
}

func (s *MemoryStore) Fetch(offset int) ([]byte, error) {
	if len(s.data) < offset {
		return nil, fmt.Errorf("Offset is too large")
	} 
	var c []byte
	copy(c, s.data[offset])
	return c, nil
}


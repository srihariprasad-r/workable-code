package main

//import "fmt"

func main() {
	cfg := &Config{
		ListenAddr: ":3000",
		Store:      func() Storer { return NewMemoryStore() },
	}
	s, _ := NewServer(cfg)
	s.createTopic("topic1")
}
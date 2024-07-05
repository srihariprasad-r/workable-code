package main

type Some struct {
	Interf Inter
}

type Server struct {
	*Some
	topics map[string]Inter
}

func NewServer(s *Some) (*Server, error) {
	return &Server{Some: s, 
		topics: make(map[string]Inter)}, nil
}
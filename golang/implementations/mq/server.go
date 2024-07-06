package main

type Config struct {
	ListenAddr string
	Store StoredFunc
}

type Server struct {
	*Config
	topic map[string]Storer
}

func NewServer(cfg *Config) (*Server, error) {
	return &Server{ 
		Config: cfg,
		topic: make(map[string]Storer, 0),
	}, nil
}

func (s *Server) createTopic(name string) {
	if _, ok := s.topic[name]; !ok {
		s.topic[name] = s.Store()
	}
}
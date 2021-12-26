package main

import (
	"bufio"
	"fmt"
	pb "go-grpc-test/proto"
	"io"
	"log"
	"net"
	"os"
	"strings"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedTestServer
}

func (*server) ControlGate(stream pb.Test_ControlGateServer) error {
	for {
		req, err := stream.Recv()
		if err == io.EOF {
			return nil
		} else if err != nil {
			log.Printf("err %v", err)
			return err
		}
		log.Printf("Received ControlGate: %v", req)
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("OpenGate: ")
		s, _ := reader.ReadString('\n')
		s = strings.TrimSpace(s)
		stream.Send(&pb.ControlGateResponse{Control: s})
	}
}

func newTestServer() pb.TestServer {
	return &server{}
}

func main() {
	lis, err := net.Listen("tcp", ":9004")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterTestServer(s, newTestServer())
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

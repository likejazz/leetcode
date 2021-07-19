package solution

import "testing"

func Test_largestOddNumber(t *testing.T) {
	type args struct {
		num string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"test", args{num: "52"}, "5"},
		{"test", args{num: "4206"}, ""},
		{"test", args{num: "35427"}, "35427"},
		{"test", args{num: "3542"}, "35"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestOddNumber(tt.args.num); got != tt.want {
				t.Errorf("largestOddNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}

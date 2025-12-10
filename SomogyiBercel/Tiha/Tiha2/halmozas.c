#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint64_t uint64;

uint64 sum_digits(uint64 n) {
	uint64 sum = 0;
	while(n) {
		sum += (n % 10);
		n /= 10;
	}
	return sum;
}

uint64 calculate(uint64 i) {
	uint64 prev = sum_digits(i);
	while(1) {
		uint64 curr = sum_digits(prev);
		if(prev == curr) {
			return curr;
		} else {
			prev = curr;
		}
	}
}

int main() {
	uint64 Q;
	scanf("%llu", &Q);

	for(uint64 q = 0; q < Q; q++) {
		uint64 f, t;
		scanf("%llu %llu", &f, &t);

		uint64 sum = 0;

		for(uint64 i = f; i <= t; i++) {
			sum += calculate(i);
		}

		printf("%llu\n", sum);

	}

}
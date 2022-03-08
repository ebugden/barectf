/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2022 Jon Lamb <jon@auxon.io>
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include <assert.h>
#include <stdint.h>

#include "test-platform.h"
#include "barectf.h"

int main(void)
{
	struct test_platform_ctx * const platform_ctx = test_platform_init(64);

	assert(platform_ctx);
	assert(barectf_packet_sequence_number(test_platform_barectf_ctx(platform_ctx)) == 0);
	barectf_trace_ev(test_platform_barectf_ctx(platform_ctx),
		"I feel special.");
	barectf_trace_ev(test_platform_barectf_ctx(platform_ctx),
		"I feel special.");
	assert(barectf_packet_sequence_number(test_platform_barectf_ctx(platform_ctx)) == 1);
	barectf_trace_ev(test_platform_barectf_ctx(platform_ctx),
		"I feel special.");
	assert(barectf_packet_sequence_number(test_platform_barectf_ctx(platform_ctx)) == 2);
	barectf_trace_ev(test_platform_barectf_ctx(platform_ctx),
		"I feel special.");
	assert(barectf_packet_sequence_number(test_platform_barectf_ctx(platform_ctx)) == 3);
	test_platform_fini(platform_ctx);
	return 0;
}

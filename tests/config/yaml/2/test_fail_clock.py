# The MIT License (MIT)
#
# Copyright (c) 2020 Philippe Proulx <pproulx@efficios.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

def test_absolute_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/absolute-invalid-type')


def test_description_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/description-invalid-type')


def test_ec_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/ec-invalid-type')


def test_ec_invalid(request, config_fail_test):
    config_fail_test(request, 'clock/ec-invalid')


def test_freq_0(request, config_fail_test):
    config_fail_test(request, 'clock/freq-0')


def test_freq_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/freq-invalid-type')


def test_freq_neg(request, config_fail_test):
    config_fail_test(request, 'clock/freq-neg')


def test_offset_cycles_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/offset-cycles-invalid-type')


def test_offset_cycles_neg(request, config_fail_test):
    config_fail_test(request, 'clock/offset-cycles-neg')


def test_offset_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/offset-invalid-type')


def test_offset_seconds_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/offset-seconds-invalid-type')


def test_offset_seconds_neg(request, config_fail_test):
    config_fail_test(request, 'clock/offset-seconds-neg')


def test_offset_unknown_prop(request, config_fail_test):
    config_fail_test(request, 'clock/offset-unknown-prop')


def test_rct_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/rct-invalid-type')


def test_unknown_prop(request, config_fail_test):
    config_fail_test(request, 'clock/unknown-prop')


def test_uuid_invalid_type(request, config_fail_test):
    config_fail_test(request, 'clock/uuid-invalid-type')


def test_uuid_invalid(request, config_fail_test):
    config_fail_test(request, 'clock/uuid-invalid')
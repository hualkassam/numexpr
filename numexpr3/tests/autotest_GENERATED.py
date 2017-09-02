# -*- coding: utf-8 -*-
"""
autotest_stub.py
Created on Mon Feb 13 09:54:32 2017
@author: Robert A. McLeod

Using the operations produced by code_generators/interp_generator.py, 

There should be two version: 
    1.) single-threaded, with a small array
    2.) multi-threaded, with an array > 4*BLOCK_SIZE, or 2**16
"""

import unittest
import numpy as np
import numexpr3 as ne
import os

SMALL_SIZE = 2**7
LARGE_SIZE = 2**17

np.random.seed(42)

# Float-64
A_d = np.random.uniform( size=LARGE_SIZE )
B_d = np.random.uniform( size=LARGE_SIZE )
C_d = np.random.uniform( size=LARGE_SIZE )
# Float-32
A_f = A_d.astype('float32')
B_f = B_d.astype('float32')
C_f = C_d.astype('float32')

if os.name == 'nt':
    # Int-64
    A_q = np.random.randint( -10, high=100, size=LARGE_SIZE ).astype('int64')
    B_q = np.random.randint( -10, high=100, size=LARGE_SIZE ).astype('int64')
    C_q = np.random.randint( -10, high=100, size=LARGE_SIZE ).astype('int64')
    # Int-32
    A_l = A_q.astype('int32')
    B_l = B_q.astype('int32')
    C_l = C_q.astype('int32')
    # UInt-64
    A_Q = A_q.astype('uint64')
    B_Q = B_q.astype('uint64')
    C_Q = C_q.astype('uint64')
    # UInt-32
    A_L = A_q.astype('uint32')
    B_L = B_q.astype('uint32')
    C_L = C_q.astype('uint32')

else:
    # Int-64
    A_l = np.random.randint( -10, high=100, size=LARGE_SIZE ).astype('int64')
    B_l = np.random.randint( -10, high=100, size=LARGE_SIZE ).astype('int64')
    C_l = np.random.randint( -10, high=100, size=LARGE_SIZE ).astype('int64')
    # Int-32
    A_i = A_l.astype('int32')
    B_i = B_l.astype('int32')
    C_i = C_l.astype('int32')
    # UInt-64
    A_L = A_l.astype('uint64')
    B_L = B_l.astype('uint64')
    C_L = C_l.astype('uint64')
    # UInt-32
    A_I = A_l.astype('uint32')
    B_I = B_l.astype('uint32')
    C_I = C_l.astype('uint32')

# Int-16
A_h = A_l.astype('int16')
B_h = B_l.astype('int16')
C_h = C_l.astype('int16')
# UInt-16
A_H = A_l.astype('uint16')
B_H = B_l.astype('uint16')
C_H = C_l.astype('uint16')

# Int-8
A_b = A_l.astype('int8')
B_b = B_l.astype('int8')
C_b = C_l.astype('int8')
# UInt-8
A_B = A_l.astype('uint8')
B_B = B_l.astype('uint8')
C_B = C_l.astype('uint8')
# Bool
A_1 = (A_l > 50).astype('bool')
B_1 = (B_l > 50).astype('bool')
C_1 = (C_l > 50).astype('bool')
# Complex-64
A_F = A_f + 1j*B_f
B_F = B_f + 1j*C_f
C_F = C_f + 1j*A_f
# Complex-128
A_D = A_d + 1j*B_d
B_D = B_d + 1j*C_d
C_D = C_d + 1j*A_d
    
class autotest_numexpr(unittest.TestCase):
    
    def setUp(self):
        # Can put any threading or other control statements in here.
        pass
    
    def test_add_111(self):
        print('Test: out=A_1 + B_1')
        out = ne.evaluate('A_1 + B_1')
        np.testing.assert_array_almost_equal(out,A_1 + B_1)
    def test_add_bbb(self):
        print('Test: out=A_b + B_b')
        out = ne.evaluate('A_b + B_b')
        np.testing.assert_array_almost_equal(out,A_b + B_b)
    def test_add_hhh(self):
        print('Test: out=A_h + B_h')
        out = ne.evaluate('A_h + B_h')
        np.testing.assert_array_almost_equal(out,A_h + B_h)
    def test_add_lll(self):
        print('Test: out=A_l + B_l')
        out = ne.evaluate('A_l + B_l')
        np.testing.assert_array_almost_equal(out,A_l + B_l)
    def test_add_qqq(self):
        print('Test: out=A_q + B_q')
        out = ne.evaluate('A_q + B_q')
        np.testing.assert_array_almost_equal(out,A_q + B_q)
    def test_add_BBB(self):
        print('Test: out=A_B + B_B')
        out = ne.evaluate('A_B + B_B')
        np.testing.assert_array_almost_equal(out,A_B + B_B)
    def test_add_HHH(self):
        print('Test: out=A_H + B_H')
        out = ne.evaluate('A_H + B_H')
        np.testing.assert_array_almost_equal(out,A_H + B_H)
    def test_add_LLL(self):
        print('Test: out=A_L + B_L')
        out = ne.evaluate('A_L + B_L')
        np.testing.assert_array_almost_equal(out,A_L + B_L)
    def test_add_QQQ(self):
        print('Test: out=A_Q + B_Q')
        out = ne.evaluate('A_Q + B_Q')
        np.testing.assert_array_almost_equal(out,A_Q + B_Q)
    def test_add_fff(self):
        print('Test: out=A_f + B_f')
        out = ne.evaluate('A_f + B_f')
        np.testing.assert_array_almost_equal(out,A_f + B_f)
    def test_add_ddd(self):
        print('Test: out=A_d + B_d')
        out = ne.evaluate('A_d + B_d')
        np.testing.assert_array_almost_equal(out,A_d + B_d)
    def test_sub_bbb(self):
        print('Test: out=A_b - B_b')
        out = ne.evaluate('A_b - B_b')
        np.testing.assert_array_almost_equal(out,A_b - B_b)
    def test_sub_hhh(self):
        print('Test: out=A_h - B_h')
        out = ne.evaluate('A_h - B_h')
        np.testing.assert_array_almost_equal(out,A_h - B_h)
    def test_sub_lll(self):
        print('Test: out=A_l - B_l')
        out = ne.evaluate('A_l - B_l')
        np.testing.assert_array_almost_equal(out,A_l - B_l)
    def test_sub_qqq(self):
        print('Test: out=A_q - B_q')
        out = ne.evaluate('A_q - B_q')
        np.testing.assert_array_almost_equal(out,A_q - B_q)
    def test_sub_BBB(self):
        print('Test: out=A_B - B_B')
        out = ne.evaluate('A_B - B_B')
        np.testing.assert_array_almost_equal(out,A_B - B_B)
    def test_sub_HHH(self):
        print('Test: out=A_H - B_H')
        out = ne.evaluate('A_H - B_H')
        np.testing.assert_array_almost_equal(out,A_H - B_H)
    def test_sub_LLL(self):
        print('Test: out=A_L - B_L')
        out = ne.evaluate('A_L - B_L')
        np.testing.assert_array_almost_equal(out,A_L - B_L)
    def test_sub_QQQ(self):
        print('Test: out=A_Q - B_Q')
        out = ne.evaluate('A_Q - B_Q')
        np.testing.assert_array_almost_equal(out,A_Q - B_Q)
    def test_sub_fff(self):
        print('Test: out=A_f - B_f')
        out = ne.evaluate('A_f - B_f')
        np.testing.assert_array_almost_equal(out,A_f - B_f)
    def test_sub_ddd(self):
        print('Test: out=A_d - B_d')
        out = ne.evaluate('A_d - B_d')
        np.testing.assert_array_almost_equal(out,A_d - B_d)
    def test_mult_111(self):
        print('Test: out=A_1 * B_1')
        out = ne.evaluate('A_1 * B_1')
        np.testing.assert_array_almost_equal(out,A_1 * B_1)
    def test_mult_bbb(self):
        print('Test: out=A_b * B_b')
        out = ne.evaluate('A_b * B_b')
        np.testing.assert_array_almost_equal(out,A_b * B_b)
    def test_mult_hhh(self):
        print('Test: out=A_h * B_h')
        out = ne.evaluate('A_h * B_h')
        np.testing.assert_array_almost_equal(out,A_h * B_h)
    def test_mult_lll(self):
        print('Test: out=A_l * B_l')
        out = ne.evaluate('A_l * B_l')
        np.testing.assert_array_almost_equal(out,A_l * B_l)
    def test_mult_qqq(self):
        print('Test: out=A_q * B_q')
        out = ne.evaluate('A_q * B_q')
        np.testing.assert_array_almost_equal(out,A_q * B_q)
    def test_mult_BBB(self):
        print('Test: out=A_B * B_B')
        out = ne.evaluate('A_B * B_B')
        np.testing.assert_array_almost_equal(out,A_B * B_B)
    def test_mult_HHH(self):
        print('Test: out=A_H * B_H')
        out = ne.evaluate('A_H * B_H')
        np.testing.assert_array_almost_equal(out,A_H * B_H)
    def test_mult_LLL(self):
        print('Test: out=A_L * B_L')
        out = ne.evaluate('A_L * B_L')
        np.testing.assert_array_almost_equal(out,A_L * B_L)
    def test_mult_QQQ(self):
        print('Test: out=A_Q * B_Q')
        out = ne.evaluate('A_Q * B_Q')
        np.testing.assert_array_almost_equal(out,A_Q * B_Q)
    def test_mult_fff(self):
        print('Test: out=A_f * B_f')
        out = ne.evaluate('A_f * B_f')
        np.testing.assert_array_almost_equal(out,A_f * B_f)
    def test_mult_ddd(self):
        print('Test: out=A_d * B_d')
        out = ne.evaluate('A_d * B_d')
        np.testing.assert_array_almost_equal(out,A_d * B_d)
    def test_div_d11(self):
        print('Test: out=A_1 / B_1')
        out = ne.evaluate('A_1 / B_1')
        np.testing.assert_array_almost_equal(out,A_1 / B_1)
    def test_div_dbb(self):
        print('Test: out=A_b / B_b')
        out = ne.evaluate('A_b / B_b')
        np.testing.assert_array_almost_equal(out,A_b / B_b)
    def test_div_dhh(self):
        print('Test: out=A_h / B_h')
        out = ne.evaluate('A_h / B_h')
        np.testing.assert_array_almost_equal(out,A_h / B_h)
    def test_div_dll(self):
        print('Test: out=A_l / B_l')
        out = ne.evaluate('A_l / B_l')
        np.testing.assert_array_almost_equal(out,A_l / B_l)
    def test_div_dqq(self):
        print('Test: out=A_q / B_q')
        out = ne.evaluate('A_q / B_q')
        np.testing.assert_array_almost_equal(out,A_q / B_q)
    def test_div_dBB(self):
        print('Test: out=A_B / B_B')
        out = ne.evaluate('A_B / B_B')
        np.testing.assert_array_almost_equal(out,A_B / B_B)
    def test_div_dHH(self):
        print('Test: out=A_H / B_H')
        out = ne.evaluate('A_H / B_H')
        np.testing.assert_array_almost_equal(out,A_H / B_H)
    def test_div_dLL(self):
        print('Test: out=A_L / B_L')
        out = ne.evaluate('A_L / B_L')
        np.testing.assert_array_almost_equal(out,A_L / B_L)
    def test_div_dQQ(self):
        print('Test: out=A_Q / B_Q')
        out = ne.evaluate('A_Q / B_Q')
        np.testing.assert_array_almost_equal(out,A_Q / B_Q)
    def test_div_fff(self):
        print('Test: out=A_f / B_f')
        out = ne.evaluate('A_f / B_f')
        np.testing.assert_array_almost_equal(out,A_f / B_f)
    def test_div_ddd(self):
        print('Test: out=A_d / B_d')
        out = ne.evaluate('A_d / B_d')
        np.testing.assert_array_almost_equal(out,A_d / B_d)
    def test_pow_fff(self):
        print('Test: out=A_f ** B_f')
        out = ne.evaluate('A_f ** B_f')
        np.testing.assert_array_almost_equal(out,A_f ** B_f)
    def test_pow_ddd(self):
        print('Test: out=A_d ** B_d')
        out = ne.evaluate('A_d ** B_d')
        np.testing.assert_array_almost_equal(out,A_d ** B_d)
    def test_mod_fff(self):
        print('Test: out=A_f % B_f')
        out = ne.evaluate('A_f % B_f')
        np.testing.assert_array_almost_equal(out,A_f % B_f)
    def test_mod_ddd(self):
        print('Test: out=A_d % B_d')
        out = ne.evaluate('A_d % B_d')
        np.testing.assert_array_almost_equal(out,A_d % B_d)
    def test_where_1111(self):
        print('Test: out=where( A_1, B_1, C_1 )')
        out = ne.evaluate('where( A_1, B_1, C_1 )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_1, C_1 ))
    def test_where_b1bb(self):
        print('Test: out=where( A_1, B_b, C_b )')
        out = ne.evaluate('where( A_1, B_b, C_b )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_b, C_b ))
    def test_where_h1hh(self):
        print('Test: out=where( A_1, B_h, C_h )')
        out = ne.evaluate('where( A_1, B_h, C_h )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_h, C_h ))
    def test_where_l1ll(self):
        print('Test: out=where( A_1, B_l, C_l )')
        out = ne.evaluate('where( A_1, B_l, C_l )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_l, C_l ))
    def test_where_q1qq(self):
        print('Test: out=where( A_1, B_q, C_q )')
        out = ne.evaluate('where( A_1, B_q, C_q )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_q, C_q ))
    def test_where_B1BB(self):
        print('Test: out=where( A_1, B_B, C_B )')
        out = ne.evaluate('where( A_1, B_B, C_B )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_B, C_B ))
    def test_where_H1HH(self):
        print('Test: out=where( A_1, B_H, C_H )')
        out = ne.evaluate('where( A_1, B_H, C_H )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_H, C_H ))
    def test_where_L1LL(self):
        print('Test: out=where( A_1, B_L, C_L )')
        out = ne.evaluate('where( A_1, B_L, C_L )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_L, C_L ))
    def test_where_Q1QQ(self):
        print('Test: out=where( A_1, B_Q, C_Q )')
        out = ne.evaluate('where( A_1, B_Q, C_Q )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_Q, C_Q ))
    def test_where_f1ff(self):
        print('Test: out=where( A_1, B_f, C_f )')
        out = ne.evaluate('where( A_1, B_f, C_f )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_f, C_f ))
    def test_where_d1dd(self):
        print('Test: out=where( A_1, B_d, C_d )')
        out = ne.evaluate('where( A_1, B_d, C_d )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_d, C_d ))
    def test_where_F1FF(self):
        print('Test: out=where( A_1, B_F, C_F )')
        out = ne.evaluate('where( A_1, B_F, C_F )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_F, C_F ))
    def test_where_D1DD(self):
        print('Test: out=where( A_1, B_D, C_D )')
        out = ne.evaluate('where( A_1, B_D, C_D )')
        np.testing.assert_array_almost_equal(out,np.where( A_1, B_D, C_D ))
    def test_ones_like_11(self):
        print('Test: out=ones_like( A_1 )')
        out = ne.evaluate('ones_like( A_1 )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_1 ))
    def test_ones_like_bb(self):
        print('Test: out=ones_like( A_b )')
        out = ne.evaluate('ones_like( A_b )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_b ))
    def test_ones_like_hh(self):
        print('Test: out=ones_like( A_h )')
        out = ne.evaluate('ones_like( A_h )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_h ))
    def test_ones_like_ll(self):
        print('Test: out=ones_like( A_l )')
        out = ne.evaluate('ones_like( A_l )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_l ))
    def test_ones_like_qq(self):
        print('Test: out=ones_like( A_q )')
        out = ne.evaluate('ones_like( A_q )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_q ))
    def test_ones_like_BB(self):
        print('Test: out=ones_like( A_B )')
        out = ne.evaluate('ones_like( A_B )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_B ))
    def test_ones_like_HH(self):
        print('Test: out=ones_like( A_H )')
        out = ne.evaluate('ones_like( A_H )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_H ))
    def test_ones_like_LL(self):
        print('Test: out=ones_like( A_L )')
        out = ne.evaluate('ones_like( A_L )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_L ))
    def test_ones_like_QQ(self):
        print('Test: out=ones_like( A_Q )')
        out = ne.evaluate('ones_like( A_Q )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_Q ))
    def test_ones_like_ff(self):
        print('Test: out=ones_like( A_f )')
        out = ne.evaluate('ones_like( A_f )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_f ))
    def test_ones_like_dd(self):
        print('Test: out=ones_like( A_d )')
        out = ne.evaluate('ones_like( A_d )')
        np.testing.assert_array_almost_equal(out,np.ones_like( A_d ))
    def test_lshift_bbb(self):
        print('Test: out=A_b << B_b')
        out = ne.evaluate('A_b << B_b')
        np.testing.assert_array_almost_equal(out,A_b << B_b)
    def test_lshift_hhh(self):
        print('Test: out=A_h << B_h')
        out = ne.evaluate('A_h << B_h')
        np.testing.assert_array_almost_equal(out,A_h << B_h)
    def test_lshift_lll(self):
        print('Test: out=A_l << B_l')
        out = ne.evaluate('A_l << B_l')
        np.testing.assert_array_almost_equal(out,A_l << B_l)
    def test_lshift_qqq(self):
        print('Test: out=A_q << B_q')
        out = ne.evaluate('A_q << B_q')
        np.testing.assert_array_almost_equal(out,A_q << B_q)
    def test_lshift_BBB(self):
        print('Test: out=A_B << B_B')
        out = ne.evaluate('A_B << B_B')
        np.testing.assert_array_almost_equal(out,A_B << B_B)
    def test_lshift_HHH(self):
        print('Test: out=A_H << B_H')
        out = ne.evaluate('A_H << B_H')
        np.testing.assert_array_almost_equal(out,A_H << B_H)
    def test_lshift_LLL(self):
        print('Test: out=A_L << B_L')
        out = ne.evaluate('A_L << B_L')
        np.testing.assert_array_almost_equal(out,A_L << B_L)
    def test_lshift_QQQ(self):
        print('Test: out=A_Q << B_Q')
        out = ne.evaluate('A_Q << B_Q')
        np.testing.assert_array_almost_equal(out,A_Q << B_Q)
    def test_rshift_bbb(self):
        print('Test: out=A_b >> B_b')
        out = ne.evaluate('A_b >> B_b')
        np.testing.assert_array_almost_equal(out,A_b >> B_b)
    def test_rshift_hhh(self):
        print('Test: out=A_h >> B_h')
        out = ne.evaluate('A_h >> B_h')
        np.testing.assert_array_almost_equal(out,A_h >> B_h)
    def test_rshift_lll(self):
        print('Test: out=A_l >> B_l')
        out = ne.evaluate('A_l >> B_l')
        np.testing.assert_array_almost_equal(out,A_l >> B_l)
    def test_rshift_qqq(self):
        print('Test: out=A_q >> B_q')
        out = ne.evaluate('A_q >> B_q')
        np.testing.assert_array_almost_equal(out,A_q >> B_q)
    def test_rshift_BBB(self):
        print('Test: out=A_B >> B_B')
        out = ne.evaluate('A_B >> B_B')
        np.testing.assert_array_almost_equal(out,A_B >> B_B)
    def test_rshift_HHH(self):
        print('Test: out=A_H >> B_H')
        out = ne.evaluate('A_H >> B_H')
        np.testing.assert_array_almost_equal(out,A_H >> B_H)
    def test_rshift_LLL(self):
        print('Test: out=A_L >> B_L')
        out = ne.evaluate('A_L >> B_L')
        np.testing.assert_array_almost_equal(out,A_L >> B_L)
    def test_rshift_QQQ(self):
        print('Test: out=A_Q >> B_Q')
        out = ne.evaluate('A_Q >> B_Q')
        np.testing.assert_array_almost_equal(out,A_Q >> B_Q)
    def test_bitand_111(self):
        print('Test: out=A_1 & B_1')
        out = ne.evaluate('A_1 & B_1')
        np.testing.assert_array_almost_equal(out,A_1 & B_1)
    def test_bitand_bbb(self):
        print('Test: out=A_b & B_b')
        out = ne.evaluate('A_b & B_b')
        np.testing.assert_array_almost_equal(out,A_b & B_b)
    def test_bitand_hhh(self):
        print('Test: out=A_h & B_h')
        out = ne.evaluate('A_h & B_h')
        np.testing.assert_array_almost_equal(out,A_h & B_h)
    def test_bitand_lll(self):
        print('Test: out=A_l & B_l')
        out = ne.evaluate('A_l & B_l')
        np.testing.assert_array_almost_equal(out,A_l & B_l)
    def test_bitand_qqq(self):
        print('Test: out=A_q & B_q')
        out = ne.evaluate('A_q & B_q')
        np.testing.assert_array_almost_equal(out,A_q & B_q)
    def test_bitand_BBB(self):
        print('Test: out=A_B & B_B')
        out = ne.evaluate('A_B & B_B')
        np.testing.assert_array_almost_equal(out,A_B & B_B)
    def test_bitand_HHH(self):
        print('Test: out=A_H & B_H')
        out = ne.evaluate('A_H & B_H')
        np.testing.assert_array_almost_equal(out,A_H & B_H)
    def test_bitand_LLL(self):
        print('Test: out=A_L & B_L')
        out = ne.evaluate('A_L & B_L')
        np.testing.assert_array_almost_equal(out,A_L & B_L)
    def test_bitand_QQQ(self):
        print('Test: out=A_Q & B_Q')
        out = ne.evaluate('A_Q & B_Q')
        np.testing.assert_array_almost_equal(out,A_Q & B_Q)
    def test_bitor_111(self):
        print('Test: out=A_1 | B_1')
        out = ne.evaluate('A_1 | B_1')
        np.testing.assert_array_almost_equal(out,A_1 | B_1)
    def test_bitor_bbb(self):
        print('Test: out=A_b | B_b')
        out = ne.evaluate('A_b | B_b')
        np.testing.assert_array_almost_equal(out,A_b | B_b)
    def test_bitor_hhh(self):
        print('Test: out=A_h | B_h')
        out = ne.evaluate('A_h | B_h')
        np.testing.assert_array_almost_equal(out,A_h | B_h)
    def test_bitor_lll(self):
        print('Test: out=A_l | B_l')
        out = ne.evaluate('A_l | B_l')
        np.testing.assert_array_almost_equal(out,A_l | B_l)
    def test_bitor_qqq(self):
        print('Test: out=A_q | B_q')
        out = ne.evaluate('A_q | B_q')
        np.testing.assert_array_almost_equal(out,A_q | B_q)
    def test_bitor_BBB(self):
        print('Test: out=A_B | B_B')
        out = ne.evaluate('A_B | B_B')
        np.testing.assert_array_almost_equal(out,A_B | B_B)
    def test_bitor_HHH(self):
        print('Test: out=A_H | B_H')
        out = ne.evaluate('A_H | B_H')
        np.testing.assert_array_almost_equal(out,A_H | B_H)
    def test_bitor_LLL(self):
        print('Test: out=A_L | B_L')
        out = ne.evaluate('A_L | B_L')
        np.testing.assert_array_almost_equal(out,A_L | B_L)
    def test_bitor_QQQ(self):
        print('Test: out=A_Q | B_Q')
        out = ne.evaluate('A_Q | B_Q')
        np.testing.assert_array_almost_equal(out,A_Q | B_Q)
    def test_bitxor_111(self):
        print('Test: out=A_1 ^ B_1')
        out = ne.evaluate('A_1 ^ B_1')
        np.testing.assert_array_almost_equal(out,A_1 ^ B_1)
    def test_bitxor_bbb(self):
        print('Test: out=A_b ^ B_b')
        out = ne.evaluate('A_b ^ B_b')
        np.testing.assert_array_almost_equal(out,A_b ^ B_b)
    def test_bitxor_hhh(self):
        print('Test: out=A_h ^ B_h')
        out = ne.evaluate('A_h ^ B_h')
        np.testing.assert_array_almost_equal(out,A_h ^ B_h)
    def test_bitxor_lll(self):
        print('Test: out=A_l ^ B_l')
        out = ne.evaluate('A_l ^ B_l')
        np.testing.assert_array_almost_equal(out,A_l ^ B_l)
    def test_bitxor_qqq(self):
        print('Test: out=A_q ^ B_q')
        out = ne.evaluate('A_q ^ B_q')
        np.testing.assert_array_almost_equal(out,A_q ^ B_q)
    def test_bitxor_BBB(self):
        print('Test: out=A_B ^ B_B')
        out = ne.evaluate('A_B ^ B_B')
        np.testing.assert_array_almost_equal(out,A_B ^ B_B)
    def test_bitxor_HHH(self):
        print('Test: out=A_H ^ B_H')
        out = ne.evaluate('A_H ^ B_H')
        np.testing.assert_array_almost_equal(out,A_H ^ B_H)
    def test_bitxor_LLL(self):
        print('Test: out=A_L ^ B_L')
        out = ne.evaluate('A_L ^ B_L')
        np.testing.assert_array_almost_equal(out,A_L ^ B_L)
    def test_bitxor_QQQ(self):
        print('Test: out=A_Q ^ B_Q')
        out = ne.evaluate('A_Q ^ B_Q')
        np.testing.assert_array_almost_equal(out,A_Q ^ B_Q)
    def test_logical_and_111(self):
        print('Test: out=logical_and( A_1, B_1 )')
        out = ne.evaluate('logical_and( A_1, B_1 )')
        np.testing.assert_array_almost_equal(out,np.logical_and( A_1, B_1 ))
    def test_logical_or_111(self):
        print('Test: out=logical_or( A_1, B_1 )')
        out = ne.evaluate('logical_or( A_1, B_1 )')
        np.testing.assert_array_almost_equal(out,np.logical_or( A_1, B_1 ))
    def test_gt_111(self):
        print('Test: out=A_1 > B_1')
        out = ne.evaluate('A_1 > B_1')
        np.testing.assert_array_almost_equal(out,A_1 > B_1)
    def test_gt_1bb(self):
        print('Test: out=A_b > B_b')
        out = ne.evaluate('A_b > B_b')
        np.testing.assert_array_almost_equal(out,A_b > B_b)
    def test_gt_1hh(self):
        print('Test: out=A_h > B_h')
        out = ne.evaluate('A_h > B_h')
        np.testing.assert_array_almost_equal(out,A_h > B_h)
    def test_gt_1ll(self):
        print('Test: out=A_l > B_l')
        out = ne.evaluate('A_l > B_l')
        np.testing.assert_array_almost_equal(out,A_l > B_l)
    def test_gt_1qq(self):
        print('Test: out=A_q > B_q')
        out = ne.evaluate('A_q > B_q')
        np.testing.assert_array_almost_equal(out,A_q > B_q)
    def test_gt_1BB(self):
        print('Test: out=A_B > B_B')
        out = ne.evaluate('A_B > B_B')
        np.testing.assert_array_almost_equal(out,A_B > B_B)
    def test_gt_1HH(self):
        print('Test: out=A_H > B_H')
        out = ne.evaluate('A_H > B_H')
        np.testing.assert_array_almost_equal(out,A_H > B_H)
    def test_gt_1LL(self):
        print('Test: out=A_L > B_L')
        out = ne.evaluate('A_L > B_L')
        np.testing.assert_array_almost_equal(out,A_L > B_L)
    def test_gt_1QQ(self):
        print('Test: out=A_Q > B_Q')
        out = ne.evaluate('A_Q > B_Q')
        np.testing.assert_array_almost_equal(out,A_Q > B_Q)
    def test_gt_1ff(self):
        print('Test: out=A_f > B_f')
        out = ne.evaluate('A_f > B_f')
        np.testing.assert_array_almost_equal(out,A_f > B_f)
    def test_gt_1dd(self):
        print('Test: out=A_d > B_d')
        out = ne.evaluate('A_d > B_d')
        np.testing.assert_array_almost_equal(out,A_d > B_d)
    def test_gte_111(self):
        print('Test: out=A_1 >= B_1')
        out = ne.evaluate('A_1 >= B_1')
        np.testing.assert_array_almost_equal(out,A_1 >= B_1)
    def test_gte_1bb(self):
        print('Test: out=A_b >= B_b')
        out = ne.evaluate('A_b >= B_b')
        np.testing.assert_array_almost_equal(out,A_b >= B_b)
    def test_gte_1hh(self):
        print('Test: out=A_h >= B_h')
        out = ne.evaluate('A_h >= B_h')
        np.testing.assert_array_almost_equal(out,A_h >= B_h)
    def test_gte_1ll(self):
        print('Test: out=A_l >= B_l')
        out = ne.evaluate('A_l >= B_l')
        np.testing.assert_array_almost_equal(out,A_l >= B_l)
    def test_gte_1qq(self):
        print('Test: out=A_q >= B_q')
        out = ne.evaluate('A_q >= B_q')
        np.testing.assert_array_almost_equal(out,A_q >= B_q)
    def test_gte_1BB(self):
        print('Test: out=A_B >= B_B')
        out = ne.evaluate('A_B >= B_B')
        np.testing.assert_array_almost_equal(out,A_B >= B_B)
    def test_gte_1HH(self):
        print('Test: out=A_H >= B_H')
        out = ne.evaluate('A_H >= B_H')
        np.testing.assert_array_almost_equal(out,A_H >= B_H)
    def test_gte_1LL(self):
        print('Test: out=A_L >= B_L')
        out = ne.evaluate('A_L >= B_L')
        np.testing.assert_array_almost_equal(out,A_L >= B_L)
    def test_gte_1QQ(self):
        print('Test: out=A_Q >= B_Q')
        out = ne.evaluate('A_Q >= B_Q')
        np.testing.assert_array_almost_equal(out,A_Q >= B_Q)
    def test_gte_1ff(self):
        print('Test: out=A_f >= B_f')
        out = ne.evaluate('A_f >= B_f')
        np.testing.assert_array_almost_equal(out,A_f >= B_f)
    def test_gte_1dd(self):
        print('Test: out=A_d >= B_d')
        out = ne.evaluate('A_d >= B_d')
        np.testing.assert_array_almost_equal(out,A_d >= B_d)
    def test_lt_111(self):
        print('Test: out=A_1 < B_1')
        out = ne.evaluate('A_1 < B_1')
        np.testing.assert_array_almost_equal(out,A_1 < B_1)
    def test_lt_1bb(self):
        print('Test: out=A_b < B_b')
        out = ne.evaluate('A_b < B_b')
        np.testing.assert_array_almost_equal(out,A_b < B_b)
    def test_lt_1hh(self):
        print('Test: out=A_h < B_h')
        out = ne.evaluate('A_h < B_h')
        np.testing.assert_array_almost_equal(out,A_h < B_h)
    def test_lt_1ll(self):
        print('Test: out=A_l < B_l')
        out = ne.evaluate('A_l < B_l')
        np.testing.assert_array_almost_equal(out,A_l < B_l)
    def test_lt_1qq(self):
        print('Test: out=A_q < B_q')
        out = ne.evaluate('A_q < B_q')
        np.testing.assert_array_almost_equal(out,A_q < B_q)
    def test_lt_1BB(self):
        print('Test: out=A_B < B_B')
        out = ne.evaluate('A_B < B_B')
        np.testing.assert_array_almost_equal(out,A_B < B_B)
    def test_lt_1HH(self):
        print('Test: out=A_H < B_H')
        out = ne.evaluate('A_H < B_H')
        np.testing.assert_array_almost_equal(out,A_H < B_H)
    def test_lt_1LL(self):
        print('Test: out=A_L < B_L')
        out = ne.evaluate('A_L < B_L')
        np.testing.assert_array_almost_equal(out,A_L < B_L)
    def test_lt_1QQ(self):
        print('Test: out=A_Q < B_Q')
        out = ne.evaluate('A_Q < B_Q')
        np.testing.assert_array_almost_equal(out,A_Q < B_Q)
    def test_lt_1ff(self):
        print('Test: out=A_f < B_f')
        out = ne.evaluate('A_f < B_f')
        np.testing.assert_array_almost_equal(out,A_f < B_f)
    def test_lt_1dd(self):
        print('Test: out=A_d < B_d')
        out = ne.evaluate('A_d < B_d')
        np.testing.assert_array_almost_equal(out,A_d < B_d)
    def test_lte_111(self):
        print('Test: out=A_1 <= B_1')
        out = ne.evaluate('A_1 <= B_1')
        np.testing.assert_array_almost_equal(out,A_1 <= B_1)
    def test_lte_1bb(self):
        print('Test: out=A_b <= B_b')
        out = ne.evaluate('A_b <= B_b')
        np.testing.assert_array_almost_equal(out,A_b <= B_b)
    def test_lte_1hh(self):
        print('Test: out=A_h <= B_h')
        out = ne.evaluate('A_h <= B_h')
        np.testing.assert_array_almost_equal(out,A_h <= B_h)
    def test_lte_1ll(self):
        print('Test: out=A_l <= B_l')
        out = ne.evaluate('A_l <= B_l')
        np.testing.assert_array_almost_equal(out,A_l <= B_l)
    def test_lte_1qq(self):
        print('Test: out=A_q <= B_q')
        out = ne.evaluate('A_q <= B_q')
        np.testing.assert_array_almost_equal(out,A_q <= B_q)
    def test_lte_1BB(self):
        print('Test: out=A_B <= B_B')
        out = ne.evaluate('A_B <= B_B')
        np.testing.assert_array_almost_equal(out,A_B <= B_B)
    def test_lte_1HH(self):
        print('Test: out=A_H <= B_H')
        out = ne.evaluate('A_H <= B_H')
        np.testing.assert_array_almost_equal(out,A_H <= B_H)
    def test_lte_1LL(self):
        print('Test: out=A_L <= B_L')
        out = ne.evaluate('A_L <= B_L')
        np.testing.assert_array_almost_equal(out,A_L <= B_L)
    def test_lte_1QQ(self):
        print('Test: out=A_Q <= B_Q')
        out = ne.evaluate('A_Q <= B_Q')
        np.testing.assert_array_almost_equal(out,A_Q <= B_Q)
    def test_lte_1ff(self):
        print('Test: out=A_f <= B_f')
        out = ne.evaluate('A_f <= B_f')
        np.testing.assert_array_almost_equal(out,A_f <= B_f)
    def test_lte_1dd(self):
        print('Test: out=A_d <= B_d')
        out = ne.evaluate('A_d <= B_d')
        np.testing.assert_array_almost_equal(out,A_d <= B_d)
    def test_eq_111(self):
        print('Test: out=A_1 == B_1')
        out = ne.evaluate('A_1 == B_1')
        np.testing.assert_array_almost_equal(out,A_1 == B_1)
    def test_eq_1bb(self):
        print('Test: out=A_b == B_b')
        out = ne.evaluate('A_b == B_b')
        np.testing.assert_array_almost_equal(out,A_b == B_b)
    def test_eq_1hh(self):
        print('Test: out=A_h == B_h')
        out = ne.evaluate('A_h == B_h')
        np.testing.assert_array_almost_equal(out,A_h == B_h)
    def test_eq_1ll(self):
        print('Test: out=A_l == B_l')
        out = ne.evaluate('A_l == B_l')
        np.testing.assert_array_almost_equal(out,A_l == B_l)
    def test_eq_1qq(self):
        print('Test: out=A_q == B_q')
        out = ne.evaluate('A_q == B_q')
        np.testing.assert_array_almost_equal(out,A_q == B_q)
    def test_eq_1BB(self):
        print('Test: out=A_B == B_B')
        out = ne.evaluate('A_B == B_B')
        np.testing.assert_array_almost_equal(out,A_B == B_B)
    def test_eq_1HH(self):
        print('Test: out=A_H == B_H')
        out = ne.evaluate('A_H == B_H')
        np.testing.assert_array_almost_equal(out,A_H == B_H)
    def test_eq_1LL(self):
        print('Test: out=A_L == B_L')
        out = ne.evaluate('A_L == B_L')
        np.testing.assert_array_almost_equal(out,A_L == B_L)
    def test_eq_1QQ(self):
        print('Test: out=A_Q == B_Q')
        out = ne.evaluate('A_Q == B_Q')
        np.testing.assert_array_almost_equal(out,A_Q == B_Q)
    def test_eq_1ff(self):
        print('Test: out=A_f == B_f')
        out = ne.evaluate('A_f == B_f')
        np.testing.assert_array_almost_equal(out,A_f == B_f)
    def test_eq_1dd(self):
        print('Test: out=A_d == B_d')
        out = ne.evaluate('A_d == B_d')
        np.testing.assert_array_almost_equal(out,A_d == B_d)
    def test_noteq_111(self):
        print('Test: out=A_1 != B_1')
        out = ne.evaluate('A_1 != B_1')
        np.testing.assert_array_almost_equal(out,A_1 != B_1)
    def test_noteq_1bb(self):
        print('Test: out=A_b != B_b')
        out = ne.evaluate('A_b != B_b')
        np.testing.assert_array_almost_equal(out,A_b != B_b)
    def test_noteq_1hh(self):
        print('Test: out=A_h != B_h')
        out = ne.evaluate('A_h != B_h')
        np.testing.assert_array_almost_equal(out,A_h != B_h)
    def test_noteq_1ll(self):
        print('Test: out=A_l != B_l')
        out = ne.evaluate('A_l != B_l')
        np.testing.assert_array_almost_equal(out,A_l != B_l)
    def test_noteq_1qq(self):
        print('Test: out=A_q != B_q')
        out = ne.evaluate('A_q != B_q')
        np.testing.assert_array_almost_equal(out,A_q != B_q)
    def test_noteq_1BB(self):
        print('Test: out=A_B != B_B')
        out = ne.evaluate('A_B != B_B')
        np.testing.assert_array_almost_equal(out,A_B != B_B)
    def test_noteq_1HH(self):
        print('Test: out=A_H != B_H')
        out = ne.evaluate('A_H != B_H')
        np.testing.assert_array_almost_equal(out,A_H != B_H)
    def test_noteq_1LL(self):
        print('Test: out=A_L != B_L')
        out = ne.evaluate('A_L != B_L')
        np.testing.assert_array_almost_equal(out,A_L != B_L)
    def test_noteq_1QQ(self):
        print('Test: out=A_Q != B_Q')
        out = ne.evaluate('A_Q != B_Q')
        np.testing.assert_array_almost_equal(out,A_Q != B_Q)
    def test_noteq_1ff(self):
        print('Test: out=A_f != B_f')
        out = ne.evaluate('A_f != B_f')
        np.testing.assert_array_almost_equal(out,A_f != B_f)
    def test_noteq_1dd(self):
        print('Test: out=A_d != B_d')
        out = ne.evaluate('A_d != B_d')
        np.testing.assert_array_almost_equal(out,A_d != B_d)
    def test_abs_bb(self):
        print('Test: out=abs( A_b )')
        out = ne.evaluate('abs( A_b )')
        np.testing.assert_array_almost_equal(out,np.abs( A_b ))
    def test_abs_hh(self):
        print('Test: out=abs( A_h )')
        out = ne.evaluate('abs( A_h )')
        np.testing.assert_array_almost_equal(out,np.abs( A_h ))
    def test_abs_ll(self):
        print('Test: out=abs( A_l )')
        out = ne.evaluate('abs( A_l )')
        np.testing.assert_array_almost_equal(out,np.abs( A_l ))
    def test_abs_qq(self):
        print('Test: out=abs( A_q )')
        out = ne.evaluate('abs( A_q )')
        np.testing.assert_array_almost_equal(out,np.abs( A_q ))
    def test_abs_ff(self):
        print('Test: out=abs( A_f )')
        out = ne.evaluate('abs( A_f )')
        np.testing.assert_array_almost_equal(out,np.abs( A_f ))
    def test_abs_dd(self):
        print('Test: out=abs( A_d )')
        out = ne.evaluate('abs( A_d )')
        np.testing.assert_array_almost_equal(out,np.abs( A_d ))
    def test_arccos_ff(self):
        print('Test: out=arccos( A_f )')
        out = ne.evaluate('arccos( A_f )')
        np.testing.assert_array_almost_equal(out,np.arccos( A_f ))
    def test_arccos_dd(self):
        print('Test: out=arccos( A_d )')
        out = ne.evaluate('arccos( A_d )')
        np.testing.assert_array_almost_equal(out,np.arccos( A_d ))
    def test_arcsin_ff(self):
        print('Test: out=arcsin( A_f )')
        out = ne.evaluate('arcsin( A_f )')
        np.testing.assert_array_almost_equal(out,np.arcsin( A_f ))
    def test_arcsin_dd(self):
        print('Test: out=arcsin( A_d )')
        out = ne.evaluate('arcsin( A_d )')
        np.testing.assert_array_almost_equal(out,np.arcsin( A_d ))
    def test_arctan_ff(self):
        print('Test: out=arctan( A_f )')
        out = ne.evaluate('arctan( A_f )')
        np.testing.assert_array_almost_equal(out,np.arctan( A_f ))
    def test_arctan_dd(self):
        print('Test: out=arctan( A_d )')
        out = ne.evaluate('arctan( A_d )')
        np.testing.assert_array_almost_equal(out,np.arctan( A_d ))
    def test_arctan2_fff(self):
        print('Test: out=arctan2( A_f, B_f )')
        out = ne.evaluate('arctan2( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.arctan2( A_f, B_f ))
    def test_arctan2_ddd(self):
        print('Test: out=arctan2( A_d, B_d )')
        out = ne.evaluate('arctan2( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.arctan2( A_d, B_d ))
    def test_ceil_ff(self):
        print('Test: out=ceil( A_f )')
        out = ne.evaluate('ceil( A_f )')
        np.testing.assert_array_almost_equal(out,np.ceil( A_f ))
    def test_ceil_dd(self):
        print('Test: out=ceil( A_d )')
        out = ne.evaluate('ceil( A_d )')
        np.testing.assert_array_almost_equal(out,np.ceil( A_d ))
    def test_cos_ff(self):
        print('Test: out=cos( A_f )')
        out = ne.evaluate('cos( A_f )')
        np.testing.assert_array_almost_equal(out,np.cos( A_f ))
    def test_cos_dd(self):
        print('Test: out=cos( A_d )')
        out = ne.evaluate('cos( A_d )')
        np.testing.assert_array_almost_equal(out,np.cos( A_d ))
    def test_cosh_ff(self):
        print('Test: out=cosh( A_f )')
        out = ne.evaluate('cosh( A_f )')
        np.testing.assert_array_almost_equal(out,np.cosh( A_f ))
    def test_cosh_dd(self):
        print('Test: out=cosh( A_d )')
        out = ne.evaluate('cosh( A_d )')
        np.testing.assert_array_almost_equal(out,np.cosh( A_d ))
    def test_exp_ff(self):
        print('Test: out=exp( A_f )')
        out = ne.evaluate('exp( A_f )')
        np.testing.assert_array_almost_equal(out,np.exp( A_f ))
    def test_exp_dd(self):
        print('Test: out=exp( A_d )')
        out = ne.evaluate('exp( A_d )')
        np.testing.assert_array_almost_equal(out,np.exp( A_d ))
    def test_fabs_ff(self):
        print('Test: out=fabs( A_f )')
        out = ne.evaluate('fabs( A_f )')
        np.testing.assert_array_almost_equal(out,np.fabs( A_f ))
    def test_fabs_dd(self):
        print('Test: out=fabs( A_d )')
        out = ne.evaluate('fabs( A_d )')
        np.testing.assert_array_almost_equal(out,np.fabs( A_d ))
    def test_floor_ff(self):
        print('Test: out=floor( A_f )')
        out = ne.evaluate('floor( A_f )')
        np.testing.assert_array_almost_equal(out,np.floor( A_f ))
    def test_floor_dd(self):
        print('Test: out=floor( A_d )')
        out = ne.evaluate('floor( A_d )')
        np.testing.assert_array_almost_equal(out,np.floor( A_d ))
    def test_fmod_fff(self):
        print('Test: out=fmod( A_f, B_f )')
        out = ne.evaluate('fmod( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.fmod( A_f, B_f ))
    def test_fmod_ddd(self):
        print('Test: out=fmod( A_d, B_d )')
        out = ne.evaluate('fmod( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.fmod( A_d, B_d ))
    def test_log_ff(self):
        print('Test: out=log( A_f )')
        out = ne.evaluate('log( A_f )')
        np.testing.assert_array_almost_equal(out,np.log( A_f ))
    def test_log_dd(self):
        print('Test: out=log( A_d )')
        out = ne.evaluate('log( A_d )')
        np.testing.assert_array_almost_equal(out,np.log( A_d ))
    def test_log10_ff(self):
        print('Test: out=log10( A_f )')
        out = ne.evaluate('log10( A_f )')
        np.testing.assert_array_almost_equal(out,np.log10( A_f ))
    def test_log10_dd(self):
        print('Test: out=log10( A_d )')
        out = ne.evaluate('log10( A_d )')
        np.testing.assert_array_almost_equal(out,np.log10( A_d ))
    def test_sin_ff(self):
        print('Test: out=sin( A_f )')
        out = ne.evaluate('sin( A_f )')
        np.testing.assert_array_almost_equal(out,np.sin( A_f ))
    def test_sin_dd(self):
        print('Test: out=sin( A_d )')
        out = ne.evaluate('sin( A_d )')
        np.testing.assert_array_almost_equal(out,np.sin( A_d ))
    def test_sinh_ff(self):
        print('Test: out=sinh( A_f )')
        out = ne.evaluate('sinh( A_f )')
        np.testing.assert_array_almost_equal(out,np.sinh( A_f ))
    def test_sinh_dd(self):
        print('Test: out=sinh( A_d )')
        out = ne.evaluate('sinh( A_d )')
        np.testing.assert_array_almost_equal(out,np.sinh( A_d ))
    def test_sqrt_ff(self):
        print('Test: out=sqrt( A_f )')
        out = ne.evaluate('sqrt( A_f )')
        np.testing.assert_array_almost_equal(out,np.sqrt( A_f ))
    def test_sqrt_dd(self):
        print('Test: out=sqrt( A_d )')
        out = ne.evaluate('sqrt( A_d )')
        np.testing.assert_array_almost_equal(out,np.sqrt( A_d ))
    def test_tan_ff(self):
        print('Test: out=tan( A_f )')
        out = ne.evaluate('tan( A_f )')
        np.testing.assert_array_almost_equal(out,np.tan( A_f ))
    def test_tan_dd(self):
        print('Test: out=tan( A_d )')
        out = ne.evaluate('tan( A_d )')
        np.testing.assert_array_almost_equal(out,np.tan( A_d ))
    def test_tanh_ff(self):
        print('Test: out=tanh( A_f )')
        out = ne.evaluate('tanh( A_f )')
        np.testing.assert_array_almost_equal(out,np.tanh( A_f ))
    def test_tanh_dd(self):
        print('Test: out=tanh( A_d )')
        out = ne.evaluate('tanh( A_d )')
        np.testing.assert_array_almost_equal(out,np.tanh( A_d ))
    def test_isfinite_1f(self):
        print('Test: out=isfinite( A_f )')
        out = ne.evaluate('isfinite( A_f )')
        np.testing.assert_array_almost_equal(out,np.isfinite( A_f ))
    def test_isfinite_1d(self):
        print('Test: out=isfinite( A_d )')
        out = ne.evaluate('isfinite( A_d )')
        np.testing.assert_array_almost_equal(out,np.isfinite( A_d ))
    def test_isinf_1f(self):
        print('Test: out=isinf( A_f )')
        out = ne.evaluate('isinf( A_f )')
        np.testing.assert_array_almost_equal(out,np.isinf( A_f ))
    def test_isinf_1d(self):
        print('Test: out=isinf( A_d )')
        out = ne.evaluate('isinf( A_d )')
        np.testing.assert_array_almost_equal(out,np.isinf( A_d ))
    def test_isnan_1f(self):
        print('Test: out=isnan( A_f )')
        out = ne.evaluate('isnan( A_f )')
        np.testing.assert_array_almost_equal(out,np.isnan( A_f ))
    def test_isnan_1d(self):
        print('Test: out=isnan( A_d )')
        out = ne.evaluate('isnan( A_d )')
        np.testing.assert_array_almost_equal(out,np.isnan( A_d ))
    def test_signbit_1f(self):
        print('Test: out=signbit( A_f )')
        out = ne.evaluate('signbit( A_f )')
        np.testing.assert_array_almost_equal(out,np.signbit( A_f ))
    def test_signbit_1d(self):
        print('Test: out=signbit( A_d )')
        out = ne.evaluate('signbit( A_d )')
        np.testing.assert_array_almost_equal(out,np.signbit( A_d ))
    def test_arccosh_ff(self):
        print('Test: out=arccosh( A_f )')
        out = ne.evaluate('arccosh( A_f )')
        np.testing.assert_array_almost_equal(out,np.arccosh( A_f ))
    def test_arccosh_dd(self):
        print('Test: out=arccosh( A_d )')
        out = ne.evaluate('arccosh( A_d )')
        np.testing.assert_array_almost_equal(out,np.arccosh( A_d ))
    def test_arcsinh_ff(self):
        print('Test: out=arcsinh( A_f )')
        out = ne.evaluate('arcsinh( A_f )')
        np.testing.assert_array_almost_equal(out,np.arcsinh( A_f ))
    def test_arcsinh_dd(self):
        print('Test: out=arcsinh( A_d )')
        out = ne.evaluate('arcsinh( A_d )')
        np.testing.assert_array_almost_equal(out,np.arcsinh( A_d ))
    def test_arctanh_ff(self):
        print('Test: out=arctanh( A_f )')
        out = ne.evaluate('arctanh( A_f )')
        np.testing.assert_array_almost_equal(out,np.arctanh( A_f ))
    def test_arctanh_dd(self):
        print('Test: out=arctanh( A_d )')
        out = ne.evaluate('arctanh( A_d )')
        np.testing.assert_array_almost_equal(out,np.arctanh( A_d ))
    def test_cbrt_ff(self):
        print('Test: out=cbrt( A_f )')
        out = ne.evaluate('cbrt( A_f )')
        np.testing.assert_array_almost_equal(out,np.cbrt( A_f ))
    def test_cbrt_dd(self):
        print('Test: out=cbrt( A_d )')
        out = ne.evaluate('cbrt( A_d )')
        np.testing.assert_array_almost_equal(out,np.cbrt( A_d ))
    def test_copysign_fff(self):
        print('Test: out=copysign( A_f, B_f )')
        out = ne.evaluate('copysign( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.copysign( A_f, B_f ))
    def test_copysign_ddd(self):
        print('Test: out=copysign( A_d, B_d )')
        out = ne.evaluate('copysign( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.copysign( A_d, B_d ))
    def test_exp2_ff(self):
        print('Test: out=exp2( A_f )')
        out = ne.evaluate('exp2( A_f )')
        np.testing.assert_array_almost_equal(out,np.exp2( A_f ))
    def test_exp2_dd(self):
        print('Test: out=exp2( A_d )')
        out = ne.evaluate('exp2( A_d )')
        np.testing.assert_array_almost_equal(out,np.exp2( A_d ))
    def test_expm1_ff(self):
        print('Test: out=expm1( A_f )')
        out = ne.evaluate('expm1( A_f )')
        np.testing.assert_array_almost_equal(out,np.expm1( A_f ))
    def test_expm1_dd(self):
        print('Test: out=expm1( A_d )')
        out = ne.evaluate('expm1( A_d )')
        np.testing.assert_array_almost_equal(out,np.expm1( A_d ))
    def test_fmax_fff(self):
        print('Test: out=fmax( A_f, B_f )')
        out = ne.evaluate('fmax( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.fmax( A_f, B_f ))
    def test_fmax_ddd(self):
        print('Test: out=fmax( A_d, B_d )')
        out = ne.evaluate('fmax( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.fmax( A_d, B_d ))
    def test_fmin_fff(self):
        print('Test: out=fmin( A_f, B_f )')
        out = ne.evaluate('fmin( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.fmin( A_f, B_f ))
    def test_fmin_ddd(self):
        print('Test: out=fmin( A_d, B_d )')
        out = ne.evaluate('fmin( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.fmin( A_d, B_d ))
    def test_hypot_fff(self):
        print('Test: out=hypot( A_f, B_f )')
        out = ne.evaluate('hypot( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.hypot( A_f, B_f ))
    def test_hypot_ddd(self):
        print('Test: out=hypot( A_d, B_d )')
        out = ne.evaluate('hypot( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.hypot( A_d, B_d ))
    def test_log1p_ff(self):
        print('Test: out=log1p( A_f )')
        out = ne.evaluate('log1p( A_f )')
        np.testing.assert_array_almost_equal(out,np.log1p( A_f ))
    def test_log1p_dd(self):
        print('Test: out=log1p( A_d )')
        out = ne.evaluate('log1p( A_d )')
        np.testing.assert_array_almost_equal(out,np.log1p( A_d ))
    def test_log2_ff(self):
        print('Test: out=log2( A_f )')
        out = ne.evaluate('log2( A_f )')
        np.testing.assert_array_almost_equal(out,np.log2( A_f ))
    def test_log2_dd(self):
        print('Test: out=log2( A_d )')
        out = ne.evaluate('log2( A_d )')
        np.testing.assert_array_almost_equal(out,np.log2( A_d ))
    def test_nextafter_fff(self):
        print('Test: out=nextafter( A_f, B_f )')
        out = ne.evaluate('nextafter( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,np.nextafter( A_f, B_f ))
    def test_nextafter_ddd(self):
        print('Test: out=nextafter( A_d, B_d )')
        out = ne.evaluate('nextafter( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,np.nextafter( A_d, B_d ))
    def test_rint_ff(self):
        print('Test: out=rint( A_f )')
        out = ne.evaluate('rint( A_f )')
        np.testing.assert_array_almost_equal(out,np.rint( A_f ))
    def test_rint_dd(self):
        print('Test: out=rint( A_d )')
        out = ne.evaluate('rint( A_d )')
        np.testing.assert_array_almost_equal(out,np.rint( A_d ))
    def test_round_lf(self):
        print('Test: out=round( A_f )')
        out = ne.evaluate('round( A_f )')
        np.testing.assert_array_almost_equal(out,np.round( A_f ))
    def test_round_ld(self):
        print('Test: out=round( A_d )')
        out = ne.evaluate('round( A_d )')
        np.testing.assert_array_almost_equal(out,np.round( A_d ))
    def test_trunc_ff(self):
        print('Test: out=trunc( A_f )')
        out = ne.evaluate('trunc( A_f )')
        np.testing.assert_array_almost_equal(out,np.trunc( A_f ))
    def test_trunc_dd(self):
        print('Test: out=trunc( A_d )')
        out = ne.evaluate('trunc( A_d )')
        np.testing.assert_array_almost_equal(out,np.trunc( A_d ))
    def test_complex_Fff(self):
        print('Test: out=complex( A_f, B_f )')
        out = ne.evaluate('complex( A_f, B_f )')
        np.testing.assert_array_almost_equal(out,A_f + 1j*B_f)
    def test_complex_Ddd(self):
        print('Test: out=complex( A_d, B_d )')
        out = ne.evaluate('complex( A_d, B_d )')
        np.testing.assert_array_almost_equal(out,A_d + 1j*B_d)
    def test_real_fF(self):
        print('Test: out=real( A_F )')
        out = ne.evaluate('real( A_F )')
        np.testing.assert_array_almost_equal(out,np.real( A_F ))
    def test_real_dD(self):
        print('Test: out=real( A_D )')
        out = ne.evaluate('real( A_D )')
        np.testing.assert_array_almost_equal(out,np.real( A_D ))
    def test_imag_fF(self):
        print('Test: out=imag( A_F )')
        out = ne.evaluate('imag( A_F )')
        np.testing.assert_array_almost_equal(out,np.imag( A_F ))
    def test_imag_dD(self):
        print('Test: out=imag( A_D )')
        out = ne.evaluate('imag( A_D )')
        np.testing.assert_array_almost_equal(out,np.imag( A_D ))
    def test_abs_fF(self):
        print('Test: out=abs( A_F )')
        out = ne.evaluate('abs( A_F )')
        np.testing.assert_array_almost_equal(out,np.abs( A_F ))
    def test_abs_dD(self):
        print('Test: out=abs( A_D )')
        out = ne.evaluate('abs( A_D )')
        np.testing.assert_array_almost_equal(out,np.abs( A_D ))
    def test_add_FFF(self):
        print('Test: out=A_F + B_F')
        out = ne.evaluate('A_F + B_F')
        np.testing.assert_array_almost_equal(out,A_F + B_F)
    def test_add_DDD(self):
        print('Test: out=A_D + B_D')
        out = ne.evaluate('A_D + B_D')
        np.testing.assert_array_almost_equal(out,A_D + B_D)
    def test_sub_FFF(self):
        print('Test: out=A_F - B_F')
        out = ne.evaluate('A_F - B_F')
        np.testing.assert_array_almost_equal(out,A_F - B_F)
    def test_sub_DDD(self):
        print('Test: out=A_D - B_D')
        out = ne.evaluate('A_D - B_D')
        np.testing.assert_array_almost_equal(out,A_D - B_D)
    def test_mult_FFF(self):
        print('Test: out=A_F * B_F')
        out = ne.evaluate('A_F * B_F')
        np.testing.assert_array_almost_equal(out,A_F * B_F)
    def test_mult_DDD(self):
        print('Test: out=A_D * B_D')
        out = ne.evaluate('A_D * B_D')
        np.testing.assert_array_almost_equal(out,A_D * B_D)
    def test_div_FFF(self):
        print('Test: out=A_F / B_F')
        out = ne.evaluate('A_F / B_F')
        np.testing.assert_array_almost_equal(out,A_F / B_F,decimal=4)
    def test_div_DDD(self):
        print('Test: out=A_D / B_D')
        out = ne.evaluate('A_D / B_D')
        np.testing.assert_array_almost_equal(out,A_D / B_D)
    def test_neg_FF(self):
        print('Test: out=-A_F')
        out = ne.evaluate('-A_F')
        np.testing.assert_array_almost_equal(out,-A_F)
    def test_neg_DD(self):
        print('Test: out=-A_D')
        out = ne.evaluate('-A_D')
        np.testing.assert_array_almost_equal(out,-A_D)
    def test_conj_FF(self):
        print('Test: out=conj( A_F )')
        out = ne.evaluate('conj( A_F )')
        np.testing.assert_array_almost_equal(out,np.conj( A_F ))
    def test_conj_DD(self):
        print('Test: out=conj( A_D )')
        out = ne.evaluate('conj( A_D )')
        np.testing.assert_array_almost_equal(out,np.conj( A_D ))
    def test_conj_ff(self):
        print('Test: out=conj( A_f )')
        out = ne.evaluate('conj( A_f )')
        np.testing.assert_array_almost_equal(out,np.conj( A_f ))
    def test_conj_dd(self):
        print('Test: out=conj( A_d )')
        out = ne.evaluate('conj( A_d )')
        np.testing.assert_array_almost_equal(out,np.conj( A_d ))
    def test_sqrt_FF(self):
        print('Test: out=sqrt( A_F )')
        out = ne.evaluate('sqrt( A_F )')
        np.testing.assert_array_almost_equal(out,np.sqrt( A_F ))
    def test_sqrt_DD(self):
        print('Test: out=sqrt( A_D )')
        out = ne.evaluate('sqrt( A_D )')
        np.testing.assert_array_almost_equal(out,np.sqrt( A_D ))
    def test_log_FF(self):
        print('Test: out=log( A_F )')
        out = ne.evaluate('log( A_F )')
        np.testing.assert_array_almost_equal(out,np.log( A_F ))
    def test_log_DD(self):
        print('Test: out=log( A_D )')
        out = ne.evaluate('log( A_D )')
        np.testing.assert_array_almost_equal(out,np.log( A_D ))
    def test_log1p_FF(self):
        print('Test: out=log1p( A_F )')
        out = ne.evaluate('log1p( A_F )')
        np.testing.assert_array_almost_equal(out,np.log1p( A_F ))
    def test_log1p_DD(self):
        print('Test: out=log1p( A_D )')
        out = ne.evaluate('log1p( A_D )')
        np.testing.assert_array_almost_equal(out,np.log1p( A_D ))
    def test_log10_FF(self):
        print('Test: out=log10( A_F )')
        out = ne.evaluate('log10( A_F )')
        np.testing.assert_array_almost_equal(out,np.log10( A_F ))
    def test_log10_DD(self):
        print('Test: out=log10( A_D )')
        out = ne.evaluate('log10( A_D )')
        np.testing.assert_array_almost_equal(out,np.log10( A_D ))
    def test_exp_FF(self):
        print('Test: out=exp( A_F )')
        out = ne.evaluate('exp( A_F )')
        np.testing.assert_array_almost_equal(out,np.exp( A_F ))
    def test_exp_DD(self):
        print('Test: out=exp( A_D )')
        out = ne.evaluate('exp( A_D )')
        np.testing.assert_array_almost_equal(out,np.exp( A_D ))
    def test_expm1_FF(self):
        print('Test: out=expm1( A_F )')
        out = ne.evaluate('expm1( A_F )')
        np.testing.assert_array_almost_equal(out,np.expm1( A_F ))
    def test_expm1_DD(self):
        print('Test: out=expm1( A_D )')
        out = ne.evaluate('expm1( A_D )')
        np.testing.assert_array_almost_equal(out,np.expm1( A_D ))
    def test_pow_FFF(self):
        print('Test: out=A_F ** B_F')
        out = ne.evaluate('A_F ** B_F')
        np.testing.assert_array_almost_equal(out,A_F ** B_F)
    def test_pow_DDD(self):
        print('Test: out=A_D ** B_D')
        out = ne.evaluate('A_D ** B_D')
        np.testing.assert_array_almost_equal(out,A_D ** B_D)
    def test_arccos_FF(self):
        print('Test: out=arccos( A_F )')
        out = ne.evaluate('arccos( A_F )')
        np.testing.assert_array_almost_equal(out,np.arccos( A_F ))
    def test_arccos_DD(self):
        print('Test: out=arccos( A_D )')
        out = ne.evaluate('arccos( A_D )')
        np.testing.assert_array_almost_equal(out,np.arccos( A_D ))
    def test_arccosh_FF(self):
        print('Test: out=arccosh( A_F )')
        out = ne.evaluate('arccosh( A_F )')
        np.testing.assert_array_almost_equal(out,np.arccosh( A_F ))
    def test_arccosh_DD(self):
        print('Test: out=arccosh( A_D )')
        out = ne.evaluate('arccosh( A_D )')
        np.testing.assert_array_almost_equal(out,np.arccosh( A_D ))
    def test_arcsin_FF(self):
        print('Test: out=arcsin( A_F )')
        out = ne.evaluate('arcsin( A_F )')
        np.testing.assert_array_almost_equal(out,np.arcsin( A_F ))
    def test_arcsin_DD(self):
        print('Test: out=arcsin( A_D )')
        out = ne.evaluate('arcsin( A_D )')
        np.testing.assert_array_almost_equal(out,np.arcsin( A_D ))
    def test_arcsinh_FF(self):
        print('Test: out=arcsinh( A_F )')
        out = ne.evaluate('arcsinh( A_F )')
        np.testing.assert_array_almost_equal(out,np.arcsinh( A_F ))
    def test_arcsinh_DD(self):
        print('Test: out=arcsinh( A_D )')
        out = ne.evaluate('arcsinh( A_D )')
        np.testing.assert_array_almost_equal(out,np.arcsinh( A_D ))
    def test_arctan_FF(self):
        print('Test: out=arctan( A_F )')
        out = ne.evaluate('arctan( A_F )')
        np.testing.assert_array_almost_equal(out,np.arctan( A_F ))
    def test_arctan_DD(self):
        print('Test: out=arctan( A_D )')
        out = ne.evaluate('arctan( A_D )')
        np.testing.assert_array_almost_equal(out,np.arctan( A_D ))
    def test_arctanh_FF(self):
        print('Test: out=arctanh( A_F )')
        out = ne.evaluate('arctanh( A_F )')
        np.testing.assert_array_almost_equal(out,np.arctanh( A_F ))
    def test_arctanh_DD(self):
        print('Test: out=arctanh( A_D )')
        out = ne.evaluate('arctanh( A_D )')
        np.testing.assert_array_almost_equal(out,np.arctanh( A_D ))
    def test_cos_FF(self):
        print('Test: out=cos( A_F )')
        out = ne.evaluate('cos( A_F )')
        np.testing.assert_array_almost_equal(out,np.cos( A_F ))
    def test_cos_DD(self):
        print('Test: out=cos( A_D )')
        out = ne.evaluate('cos( A_D )')
        np.testing.assert_array_almost_equal(out,np.cos( A_D ))
    def test_cosh_FF(self):
        print('Test: out=cosh( A_F )')
        out = ne.evaluate('cosh( A_F )')
        np.testing.assert_array_almost_equal(out,np.cosh( A_F ))
    def test_cosh_DD(self):
        print('Test: out=cosh( A_D )')
        out = ne.evaluate('cosh( A_D )')
        np.testing.assert_array_almost_equal(out,np.cosh( A_D ))
    def test_sin_FF(self):
        print('Test: out=sin( A_F )')
        out = ne.evaluate('sin( A_F )')
        np.testing.assert_array_almost_equal(out,np.sin( A_F ))
    def test_sin_DD(self):
        print('Test: out=sin( A_D )')
        out = ne.evaluate('sin( A_D )')
        np.testing.assert_array_almost_equal(out,np.sin( A_D ))
    def test_sinh_FF(self):
        print('Test: out=sinh( A_F )')
        out = ne.evaluate('sinh( A_F )')
        np.testing.assert_array_almost_equal(out,np.sinh( A_F ))
    def test_sinh_DD(self):
        print('Test: out=sinh( A_D )')
        out = ne.evaluate('sinh( A_D )')
        np.testing.assert_array_almost_equal(out,np.sinh( A_D ))
    def test_tan_FF(self):
        print('Test: out=tan( A_F )')
        out = ne.evaluate('tan( A_F )')
        np.testing.assert_array_almost_equal(out,np.tan( A_F ))
    def test_tan_DD(self):
        print('Test: out=tan( A_D )')
        out = ne.evaluate('tan( A_D )')
        np.testing.assert_array_almost_equal(out,np.tan( A_D ))
    def test_tanh_FF(self):
        print('Test: out=tanh( A_F )')
        out = ne.evaluate('tanh( A_F )')
        np.testing.assert_array_almost_equal(out,np.tanh( A_F ))
    def test_tanh_DD(self):
        print('Test: out=tanh( A_D )')
        out = ne.evaluate('tanh( A_D )')
        np.testing.assert_array_almost_equal(out,np.tanh( A_D ))

    

def run():
    from numexpr3 import __version__
    print( "NumExpr3 auto-test for {} ".format(__version__) )
    unittest.main( exit=False )
    
if __name__ == "__main__":
    # Should generally call "python -m unittest -v numexpr3.test" for continuous integration
    run()
    
    
    
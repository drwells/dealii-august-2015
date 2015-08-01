// this is the main working loop for all vector sums using the templated
// operation above. it accumulates the sums using a block-wise summation
// algorithm with post-update. this blocked algorithm has been proposed in
// a similar form by Castaldo, Whaley and Chronopoulos (SIAM
// J. Sci. Comput. 31, 1156-1174, 2008) and we use the smallest possible
// block size, 2. Sometimes it is referred to as pairwise summation. The
// worst case error made by this algorithm is on the order O(eps *
// log2(vec_size)), whereas a naive summation is O(eps * vec_size). Even

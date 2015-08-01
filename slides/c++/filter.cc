class LerayFilter
{
public:
  LerayFilter(const double filter_radius,
              std::shared_ptr<SparseMatrix<double>> mass_matrix,
              const SparseMatrix<double> &laplace_matrix,
              const SparseMatrix<double> &boundary_matrix);
  void apply(BlockVector<double> &dst, const BlockVector<double> &src);
private:
  const double filter_radius;
  std::shared_ptr<SparseMatrix<double>> mass_matrix;
  SparseMatrix<double> x_system_matrix;
  SparseMatrix<double> other_system_matrix;
  SparseILU<double> x_preconditioner;
  PreconditionChebyshev<> other_preconditioner;
};

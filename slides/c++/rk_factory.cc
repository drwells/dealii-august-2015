std::pair<std::string, std::unique_ptr<ODE::RungeKuttaBase>> rk_factory
  (const FullMatrix<double>              &boundary_matrix,
   const FullMatrix<double>              &joint_convection,
   const FullMatrix<double>              &laplace_matrix,
   const FullMatrix<double>              &linear_operator,
   const Vector<double>                  &mean_contribution_vector,
   const FullMatrix<double>              &mass_matrix,
   const std::vector<FullMatrix<double>> &nonlinear_operator,
   const POD::NavierStokes::Parameters   &parameters);
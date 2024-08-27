
namespace CleanCode.SwitchStatements
{
    public class PayAsYouGoCustomer: Customer
    {
        public override MonthlyStatement GenerateStatement(MonthlyUsage monthlyUsage)
        {
            var statement = new MonthlyStatement();

            statement.TotalCost = 54.90f;
            
            return statement
        }
    }
}

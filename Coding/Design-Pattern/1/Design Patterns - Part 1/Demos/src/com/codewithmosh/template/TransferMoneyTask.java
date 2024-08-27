package com.codewithmosh.template;

public class TransferMoneyTask extends Task {
  // 注意：这里也是 protected
  @Override
  protected void doExecute() {
    System.out.println("Transfer Money");
  }
}

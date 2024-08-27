package com.codewithmosh.template;

// 因为protected abstract void doExecute(); 是一个abstract方法，我们需要将类的类型定义为abstract
public abstract class Task {
  private AuditTrail auditTrail;

  public Task() {
    auditTrail = new AuditTrail();
  }

  public Task(AuditTrail auditTrail) {
    this.auditTrail = auditTrail;
  }

  public void execute() {
    auditTrail.record();

    doExecute();
  }

  // 使用 protected 的原因：如果使用public，外部可能直接执行doExecute，跳过auditTrail.record();跳过我们设置的template，这是错误的。如果使用 private，abstract 和 private 有编译冲突，因为private 方法，不会被子类继承，无法被重写。protected 类似 private，但是可以被子类访问
  protected abstract void doExecute();
}

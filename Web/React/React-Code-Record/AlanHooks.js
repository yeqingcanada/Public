/* 使用 hooks */
const { handleUpdateInvoiceClick } = useHandleClickFunctions();

handleUpdateInvoiceClick({
  updatedInfo: selectedRow.updatedValue,
  originalRowInfo: {
    invoiceID: selectedRow.rowInfo.id,
    projectID: selectedRow.rowInfo.project.id,
  },
});

/* 创建 hooks */
export function useHandleClickFunctions() {
  const dispatch = useDispatch();

  const handleUpdateInvoiceClick = ({ updatedInfo, originalRowInfo }) => {
    if (!originalRowInfo) {
      toast.warning("Please select invoice!");
    } else {
      dispatch(
        updatePMInvoice({
          originalRowInfo,
          updatedInfo,
        })
      );
    }
  };

  const handleDeleteInvoiceClick = ({ invoiceID, projectID }) => {
    if (!invoiceID) {
      toast.warning("Please select invoice!");
    } else {
      dispatch(deletePMInvoice({ invoiceID, projectID }));
    }
  };

  return {
    handleUpdateInvoiceClick,
    handleDeleteInvoiceClick,
  };
}

//
//  ___FILENAME___
//  ___PROJECTNAME___
//
//  Created by ___FULLUSERNAME___ on ___DATE___.
//  Copyright (c) ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
//

import UIKit

final class ___VARIABLE_sceneName___ViewController: UIViewController {
    
    // MARK: - Outlets

    // MARK: - Properties
    private var viewModel: ___VARIABLE_sceneName___ViewModelProtocol?

    private var customView: ___VARIABLE_sceneName___View {
        // swiftlint:disable:next force_cast
        return view as! ___VARIABLE_sceneName___View
    }

    // MARK: - Lifecycle
    init(viewModel: ___VARIABLE_sceneName___ViewModelProtocol) {
        self.viewModel = viewModel
        
        super.init(nibName: nil, bundle: nil)
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func loadView() {
        self.view = ___VARIABLE_sceneName___View()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupViews()
        bindViews()
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        
        // viewModel?.handle(action: .backButtonDidTap)
    }

    // MARK: - Methods
    private func setupViews() {
        
    }
    
    private func bindViews() {
        
    }

    // MARK: - Actions

}

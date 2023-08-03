%define base_release_version 7
%define full_release_version 7
%define dist_release_version 7
%define upstream_rel 7.2
%define centos_rel 2.1511
%define dist .el%{dist_release_version}.centos

Name:           centos-repo
Version:        %{upstream_rel}
Release:        2
Summary:        Base and Update Packages for Enterprise Linux repository

Group:          System Environment/Base
License:        GPLv2

Source0:        CentOS-Base.repo
Source1:        CentOS-CR.repo
Source2:        CentOS-Debuginfo.repo
Source3:        CentOS-fasttrack.repo
Source4:        CentOS-Media.repo
Source5:        CentOS-Sources.repo
Source6:        CentOS-Vault.repo
Source7:        EULA
Source8:        GPL
Source9:        RPM-GPG-KEY-CentOS-%{base_release_version}
Source10:       RPM-GPG-KEY-CentOS-Debug-%{base_release_version}
Source11:       RPM-GPG-KEY-CentOS-Testing-%{base_release_version}

BuildArch:     noarch

%description
This package contains the Base and Update Package repositories for Enterprise Linux.


%prep
%setup -q -c -T


%build
echo OK

%install
rm -rf %{buildroot}

# create /etc
mkdir -p %{buildroot}

GPG_KEYS=( %{SOURCE9} %{SOURCE10} %{SOURCE11} )
REPOS=( %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} )
DOCS=( %{SOURCE7} %{SOURCE8} )

# copy GPG keys
mkdir -p -m 755 %{buildroot}/etc/pki/rpm-gpg
for file in "${GPG_KEYS[@]}"; do
    install -m 644 $file %{buildroot}/etc/pki/rpm-gpg
done

# copy yum repos
mkdir -p -m 755 %{buildroot}/etc/yum.repos.d
for file in "${REPOS[@]}"; do 
    install -m 644 $file %{buildroot}/etc/yum.repos.d
done

# copy the EULA and GPL License
mkdir -p -m 755 %{buildroot}/%{_docdir}/centos-repo
for file in "${DOCS[@]}"; do 
    install -m 644 $file %{buildroot}/%{_docdir}/centos-repo
done

# create yum vars
mkdir -p -m 755 %{buildroot}/etc/yum/vars
cat >> %{buildroot}/etc/yum/vars/infra << EOF
stock

EOF

# set up the dist tag macros
install -d -m 755 %{buildroot}/etc/rpm
cat >> %{buildroot}/etc/rpm/macros.dist << EOF
# dist macros.

%%centos_ver %{base_release_version}
%%centos %{base_release_version}
%%rhel %{base_release_version}
%%dist %dist
%%el%{base_release_version} 1
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_docdir}/centos-repo/*
/etc/pki/rpm-gpg/
%config(noreplace) /etc/yum.repos.d/*
%config(noreplace) /etc/yum/vars/*
/etc/rpm/macros.dist


%changelog
* Tue Jan 12 2016 John Siegrist <john@complects.com> - 7.2-2
- Added missing definition needed for proper dist macro configuration

* Wed Dec 30 2015 John Siegrist <john@complects.com> - 7.2-1
- Initial version derived from the centos-release spec
